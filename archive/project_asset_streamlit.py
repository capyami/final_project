import yfinance as yf
import pandas as pd
import datetime
from datetime import date
import streamlit as st
import numpy as np
import statistics

st.title('Investments')
st.markdown('Description')
st.image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAT4AAACfCAMAAABX0UX9AAABmFBMVEX////1gCTxfyH4giT7gyWpoaEAAAD9/Pz08/Ph4OD9hCX29fX5+Pju7Oz4giDp6OibgHXZbxBhLgDW0tK7urrd2dl0aWleUFDGxcWkoqJnY2NpXVytpqWakY/l4+PLZg+ENwA+Nzd6YVeEeHZ3MQBgV1hub3RbSETldyGdSwDEwMCLhIRCFwDAYhqsVQy8Xgi2Xx55VUImLTWTlZioVRjYbx8aAABOQ0MnAABOKA+6inOFMwAfAAC8YBuOPwD/07CCQBOMdGw3KCieUBcwAACjYj6mdmCRSBW6ajlBP0KkXzKkj4hvNQ9YJQAQAAAgEhKklJAsFhVLFADAaC19VD64dlGdeWYyEQZtPSFJAACiWiiNWz13Px1TCwBJNTJcPjRdHwBcNCGXX0A3ICCAbWdKKAqBRxpcEABUMyZvKACJZFKRYUdoNxwkICTfeS96KQC3nZOQMQCnRACBg4fDoJHCiGrCdUaojoGsYCrOXQBwFwA4DgBsNACsbkhoU0pRPjxONChFR09sRjUYGCHUp4t2V0jxv5+ka0o4u+6sAAAgAElEQVR4nO19jV/aWNp2yIeBEECaDwLkEDViY2KArkTKTHERVukotlodddTVan3cjrrdfae7U/dpx876TKf/9nvOSUBUVJjSr5lev6mDQSC5uL/PfZ8QxBd8wRd8wScGXv3YZ/A5Q7j91y3pY5/EZwu1mOEy218E8Dch9PyxQ/ko7UhnP/apfIaQCgMkRfrgv4F04GOfTPcI8Y1HfBDhw346L/7Fpn0uuMyY+LkJoJkE0GizAUWNWxjjqhL6YJ8esb53OB9F0xxHUxTnPLY+3Gf3AtKOlj0RrXRMZkRFQDCZZNr6QG5QiE06ZYN2arl6vWzY9XpuMvFZeWA9w9GZLTXi58+O8REwKPNXv6ZnUFezlNFXJu35ctGo11ftnEZlnogf4JN7BD4dhjanfClmYK3Ce7+KkP7Y4CB9fVUN0sfl6/dKBjwZ56+W/31/dK8glpHNNjaES88oMeb9frSShB7XRxlj9b7qrfJqtZjPrRZt6IGNyfTl0/kkIRQ0CtJHaf2Xv3BhsGP5S0lS1yEH83PGBz+bMorO/IN6eczWoODV6iT6OjNbn4UC64UYClgpiiynLj8bGOzIikvJwUIsVhhMd2Pz/fojg0JUQfoMo68OlZfWimS5TMII0Ec583oXb/aRoKZZcdQwopq2Dtp5CjN2cxQhyQUVh4pBNSZ3TKByMgAjFZqGEQtZMzi7mqtxSPbgY3yQowduf/IeGMYIIfVwtx+oZvtoVY/f9BZiLN6Ms3km3WHaqk78NT+Kkc8g5DOjmeZj95n8d5VPXIFDaSRyqRROO0AizRCJREI0E+m06f2FEItc/xbCotL6q7LYmc1XATM4Hh8fj48kGAhrED0e/wagX5IJ9Is1yIBPnL5ArEVjC6pUkR4I4kOg82xDFlnrejpShQvPS5VOXUgC+yoFi7eQRD9DMv6uGHxIinX4Ph8NvCi3qGxB9BfEh4L0MJ42zyRKvd6CWwD9ZFMBDPQYdFo1uZo+HC998vSpchK0/JpO6Olgn57W44X4mcUz5eveQophf+2PDRYKlco99DgU6zBk+8zpU2KBQGtxJQakCNGnSsG41XI0ELtOmESP/4DVl4ykXLWNd+g9PnP6Lp5fAV12n3BB/VLX0cfqrnH3Vx4+fPDwYR/+xdQ7S5Y/c/pShfO/jyODZ0EJMtUWxoT0NfTxsquorGkmHzKiK3aC3FnC+pnTRwx28keidc2TfNpNVVhBrCQaByPJzgp2nz19nSiZdV3sxSdd6eP1Pr0pclLyjyF9SdN/Y11eSrZJhZtgdS/CkQbPLIGgd1bt/9zpUxKyztwgKdb1SRvTeFrsAw0bqYLOAr/PnT7CLylW8tooTbwhZxPkhp2zHnhaHpTNK//8HD57+iBYsVBgrqxsCDdlsKEm++xExX0opW/Ikhv4PdAHoViVK0hS2pb7mNakVnnS0P6Im/2yi53m+V3TZ7atqX186BfUjU1h6xVJtlVD+Rw/4+ejPL8OiA7RPX3Wp0kf48a7ogKzfslUgVzAFk2S2wZw+rkKFQuSLcoakq2OV7m7pk/p+Jv5sBDxJYhPXhcKhdeyLqZ0fAHi+OU/VSuDDyuDrfkKDyrq2bNW5y0K3dEnDg5WHg4Odv7tvDP8KZYPdHI5Co7UYmdSpWB+roiYz0sfREqu6KYkmXpF7ma56FOXPmUCWA86uSAcfqRac7hBeGnsFYuF8mVWBRVYFlC7W1z85G2fnEx39IVF5NSFuqgM9dF/RbEA9GgFJ4HfXsGaL2H6gq4bUvGh1EenL50sdERfSJZg/tXKipKA/64olPK9MD/y4OCDQQRk0OBP95cJ/PNh89D5wjX/YVu/lIquP+gofQemK4FnKLCE/p57DD51BKCNNzsqHpmyap2PSXVL3bquWPAFLeAF0zyfaqVM86KD/YIv+IIv+IJPCiHl0ywmfBaQ9IeJz6udvB1CH+US/EK6IjPpj97MywqKByEYgf+6fb0IFjqs0p/7VMUMsUrzk7tPaMS+hESII91/co/B9g95mEopQ1MdVtwbkHQ1FRGtLl8FI869N0JQbnzyXPdC5AcVhbCuW4z+QGCbQI+7emlowU35QrrangC1QAQKbbMY99POPrlrhBa3dLm3pSz/FXg/Obdf2GuqrTnXdiApaBUS72elgk0uDqb7ejmKGRnvvwK6+h6KtSZoXSxmVaZdtif1Db6fYb/44pO4X+xheu7Xs9GrMPAbrPv1YGWQItSRcUxOJD4yToSYy20GgYJl9dY7en5eqSx22JHUKZR18ipQxlpPP4oIqskUISXzYWf39M6d0w0tbJ8oRHDvogk0AdTfrv3KNVAGJ5CQBwpbgz2Ol8TMlfSR4Vu9/KSgootEYKFs0D6Kw6B8NFmbEwhTV95rbdOfgLwJBKsvTvRan8RHZQNJGknh/yB8BtZcLdxb+gSgRvzqhkZRvlZQ2nQ8wqsL73OsCty9N3EvFmIe3Ov58pGYKdcga8X/Kdb+p1j1QSLtN1MIe7PhXtK3h2ZWA4Uo7bsAmrSHVCKlyu9NAKWJRUvsW4w9rPR+7FPMhothkuyr5+rFcl+JIsPH8SAKW4TN3kkfL3rdLaHt8EX6oAByuW01CWKg5wT6LUhYcOsJDCLFh5WtgmDdu3v3bqWHpV0xS2H6Vsv1W85qFanv/t2/QKz+dtsnCYLQGnj49eZ6Nche0F0awqdtgBDBMrLaYwLB4pOCBJ6geSMeJBfF+He24ziTW72zFA366na9WO2zofIu9eOM0qz9Zvr0vb2hVisT2H/R+MKtaCt9kLgfRkerZW+aJgAu9s+8G4TK4OKTwcEneAnOb5r8SJZG84yPejd/1KCvytX7+srIidiJOML42m+2fSGI1lgklSNnx91l7jWuRfKozN/6pYheOau/6Q867JbsCFtPnoC+wuuJRrDiH8HjtORAz+kLQ7+L/C+ChkftRnsXuKRyNGfsw+hOKUR9TemjnDV4GUq6ucLJC7dlQpKvCmJSkUiqq6jNmlg0UaTcNHUefb6e0oddR0uwbI9g6Yvv95I+aOTsGYUNWMdOw/eSTyVCsKxmBiWAsj0LAoTKtJ3XZGVZTnaTrQqVCpoZkWDAp4iiKLDvhz7nvdMXyHE4QjmGIbIyVeXwNdCjih/ozZpdCMjDPpqyD8f5kNq2swOZhC5cSyj5pJE4x8eGB76vCO+FvsliHtFHhcMNFh034zV6J32bURqfNzkNeF5c0xCB3IAYE5sW0oyJka85xLGWFAn/HvPOJjBQ6GuwNJbxkb5R+b3Q96iEaIvmDg9mtfeVtPmfVw1s9DhyWeQJ69DhSG276SXYQNLyE5GvsVpT4dE9iZD2zHcNYqSmCI/ZtI/OJN+T7YOil5HjUkDUZ7ukLxiR8E44oZui+cBsNWfgTSR8pRWFkKzS/tnoL4xXoHWPnDZiGs6pMSleBb+hGN8eYzb1/uiDNJV07NL48Vq4c/p40Zo62J2G2J2aen59bVBaIu1aCRs92jheUEDiLFhhdCRo5onWzOcomDgKhKSCdyyPhEwRe933TJ9xFCGEZAy6taTm65Q+v56PogIDtmkGmbl2MlJaoikjVzZQvYDyOWsPzvxtWoV51cL2ems8TR8j28cG9HeqC5t/f/L0IWqrfL/0hXMMId2KhgdUQiqHO6YvOfssGnX/MBp1frx2HiuwRCO5q+UdbAGragHX89jI3uOBgeF/fJ0Nc63ZCNdYCzN15TdrcOhPGY6jv4u/b/qojECImTAZneODwx3TFwKCqf7zK4x/qmIKXEOfX60ZNFZKaAKhGa9GWDXJ+EPMYgYX/ujzibAv3FgL48GDNgosCDyRujHvD/wJenJqdPz906cQymg4rAGW74I+vHOUu6iEfk9cszqhvNZnsngPILJUszmuCv82wKQtUdmwwxeow9LnibKYHP3+Mn3KYEUl9MKl4xfwweiz54jQ0GjmFArhesf0EWIMCF7cFlQWDqvb7buYg2CPVZ7dlxc2sOXzkfkyWcXsME8Z1s+cGtQlAmkHbTGUkutR+utL9AX1pF4AD240ix+KPpIcVqB+MRHCv91N4GLu//CP/zdZrU7+8MN/wqRRbVfKDZl7SkjfW+LI6YXktOG63to81jzVdjYF3v98tiURdh1vdNqKhMDfshzFtaOvci+Rrtx4ZR+MPp9ziq9HknNdBC6ECMR//fvHH3Ol3I8//vuFOn5ZHljTwiU84UXOx9kz+soxiUygz36jQlbUHBc+fqEQZj86TNEcF0ZWkDbyUwovnmbQ33JfX14Zk0Ac3FNF8YY1sw8nfWFnY2RcfP6mFO5G+kR4FqFAQJCEQAAGzsIl+gJ6YyDQr+xqHHl/avxtFtk62jhKmpA+SJrxEwjx4nKJi9b2p3fLtSiXPRBZITnpoDyZoofbBUR8Utb7HsSvd8ofiD63SkXaueiFnO0G+oTtZTHYzLtYM3nRFzKt7fdBdYMMU7N7C/vI1nEHop5kclgUyTsiy4NtIPE8H5T0bRDk9SOsz5RPO9KFscsXq/SBQSDfsDqS+hO0FdQApG8rg+ljifFh9JUYj3tHn9lYqKTCF9kjyaNrXsiDDPmfH6q7Mwi75f/dOV8oDoow5g0AJQBVzB+BD/iQdd/gyMM5+X6U4g4DhJled/O4sH3Ymp/51ccZDpMXnRxRF74fuGwU5ETImhi8qeRu3Z2cHPg/eFrqy4HJgVURbT/4eHJy8lGid2vIqYNo+ApQo3PXvJBnwD+/+nEpi7D07b/+aZ3f3AswIX98185P9zPq3MyxfdwPo6P+HOTqK32lFIb0QYZnMpTrTHJzzUFpcWgUxYg+mhwdAvHljC9/mb6ARATNG8eVgqjshr5UXkQPkBGQ0CG1lzMU5vzw8OarzeFz2KzDI9/vXZdz8oxE+AMSRiDCE2qL9IUsGESLskbStM/RNAeqLfSmz0O8sOlwxtIeeHsHXwLIlLGJg5HKT+4MVSBRdvWWsx8vMIkfoKa3oe9TAs8qcf+4yfJnICwlmL5pnkrVpaC7eRp8aVA5m4+EGQVM+PfypFuAoty4jqKMbTXIg2mDJmdji0kkPOOGUau6iTBlLIssuzevuWlxdHNbOqmjpz51+tDOU9aFdjoxFrt5N0vB0nVLV9F8pK6DRhjBKzjR39Y43wVQ4dKyQgSsnMNtjrxehAI6Dq2gU7Y9E1haPhrF6RtljCbjOOxDvE5+6vQRQvyCGWbFKzoXLyAUQU26UuQsuIBGD4uhdGBczsZo4xiIwBrKz0PVvrcn6sg3+nLVEhZQLm/jYIXMrInWwSgWXs6ovvkMN6b/jeAZK+WpvFi6SB/UYi48H4M+OH7PJELqvdcVXLanjBI0gTC2qKJ9ZTntMcPINVy/goavOPYHGvcKHEw1pNa0W9tZYHhHRnO5/Gt3j/5QUg8Qfjm5N42K+Ggn3qoB6dNoX7QcU/T5qFcYHKsbk921BPAoBgoJn+fkRupbY1fFUZV04FAt5GnVKQskY2f7e1t3VV6ZnGaG7rthil0rGXnHyAzp4vcZ15k45XqO47qlL2lJgtzhzk6fGlLfhn3aDGopuZ05cx2U8cOcQoQAaDIRGtcVk9E1bmnlebOUVa3XNgFohn21ehWaP7pL+gipki6kP9O5F0QfTZZ0gRCGMs1KHomcJ5M8ax8Q09nDcWj9lg3O+DEJYKKLSa4VC8l9V29pu1jGi3PdSh+Ua0H9RPcguRGIPqSr1f4gYSajpBvxaXFCiDENc8QK6ToJw+IjheX1n8hweGNhb5rEJpDL5910zakXDRrLpPZztzMjhddbic9Td4nQjNs9yhm7op+w3rpBcAkAvRlXBoAlrhgor6jBPE7oXyI5Z2ZhaMnAf5lHVQSnWsy55k8r93W5lQQvJ0wx1stGow8JcbOKTRdF2Suokxntik7W5WbXCg/JIwK7Bo4Co7MgxSozNkcu9VszWRjYQPooMj/vvgdtVF/O/7VLM8aL8AUR8/P0vISUKx2567kUuWQFiMCdXGZebOqSGUPhOJNxrSJFRofirJ+BHBs/yepklCvlObtYd7AvoXPFvip5udr8e4Zgc1StjK8f+pD1uUggfbY5kySjRkX/1OhZkxqX3RKIiDVLcuQG0I/ztfKYg80f6bxcLRt0m2J91wiJumWGWL9gyUzk09ZqwaZ83LNy1W1D45ydsyWdVFxW/IKibmZaF8S1KWTcxBfQBNorey+LeexuKKfWV7ah/WuzVNQtlJilqlbaSuqqCNIfb2N7CTRxZUYs2W4Mt+nSwK2Py+6aLRsfutU/NzWbyRqt2Ygx42a0fvHtMx+5X8P1K9pXK47l8d9dL31nJwSu9s8An4Ag4gCI+Xj39YioTVzZgsyMuobPOD6y0bLPuhAC6C5Gwu1jwzCiBnlhUS3a7C0Vfs5zVZTowZhvfrHmlrHo0l+uo89snhBzdahybiN461PerSdoyeqhu+xIG+W64eNqAtreKp2UwYHmu7yg6zMO3cAkAv5Wq3K49OLMLx4Znv0bm//unWfQ+Nbdygof7KYoPNSHVHcBQOBwRUgtrLtJBFcqV411rDLgVGFT4+vOpRKgj3b6JWTcjzK+Ug1KH+dUJ+o5n2f/innfpCq+68pEy95uwY427+4JIsmIlOjuu5fuG0tACqz84Np/Mlc+wqcu2vYLFCJ7BegW5aXsOxLMT0YNqKdH2aqdP7qbdxfTof2DllA7MEXrHeul4CyHE6+9o0NvEddvXMy6AOk+5zPeAkJY1tyE11j/LzKTosYZs3qQVU7QccoDNG3GKRPkT9aQvlP2nHk0tuoFfTD8KzpUeAP5qCDT4c7iV51VGlpWBYo4Qbxbx1t3EMRu7x8n3Q/DK48uKzyz4Sa83HJBliB9MJwh0WjC+IFGGc4zCMfxGdMjrH/hr25Rns4/Na1bWiPnHSvBULqxRB6CAdsVH8kXCkokedVuvi5iIgHihJkmpA+nu0QopqixCw4toojCNZRKSxwSKir3QonMHSMTGD4ImDEwjlf3aXsGJmxgtl8VIeJgfUoh1NNJrNCUkX9afDzqeh2n+rJqhHMvWjhRroqV1L/r9+7F0tf2W5lJSZCh04XfQsdX/84IwrO/MKICCvfuLSauHpwKHWT/E0UNe8bSeCBw8IOPCh+kiJT6YJJ2vbE9JxCCF4rwAi88H3BwgMLl1haPykUH1wmqxTI0ersKHxn3ZC4wHuLFS7ugws9jQEVnBSViTljXbFPJigkYPaVB4t379d8BvN4HUn4p2dc2cmelhX4dZkcL/QcHG3Y4+lb1C5saog+GLnuvME1QyGbPDAJvHWk+t648/3Q1R+YhffBxEd05cVf1s/Fl441sAaDLy84dlQiBoYtxAJjYcvWDBVuVa/Yf9ycePITo7DZ87wtxr3gU77u0TO+XGF0k2FAkEohEQkjXVp5l94VQfPoAZxVWdLPqeKWsmorFLyR+l8ElPdqpLe7UDM6H6HPKxSpnHFt+XlgucWjqPBxGc+dc5o7AhuSF80G0DnMIf3zwHtoKVClcTV/8rgPfhHzUxUbHPUekAAjcD8+nL2Y+ggopEcSFw9nZ49nZ3TlVgFnYVzY0gfptdEcZwiJ99qabhkFFXTFZQhya9KpSueKTfbwonC/a1SJMN3IvRELpX/edC3JQ/UEgVHDOdYqFACH/pZp/DF0HuCbIEkcNR3OM7PhHVF5pUSAYtEkuNIHnn1GZFCHo01nHgKIS5khHm4WyGBInjc0+YCYZRB8MUnKbJZ+X0c3pZVdvaXtz8cjGTpqurhbrDvXs0OSD1rRzMUOhfNoOukthy63ghEIiaE7YFOd8L7PixJVBCWu9fHy6vfP4u495J1ppEaqIugUfMef9P1paiJ8aKJ7zkW4ZiiLL8FSF40kpJksgJkDpQ30YtbrhGrvspNeZUf/5SdXllKrN10s+Z+2JHhRPLvSbuvKXx0XXkNUY9wgWYhEicQuNcuXu8tCmXLGerg4mFH+QDwYFfbD3E+tnuP6tpXsN16ef2yRZUKHlnsRhMlUq9q3Ol6u24wvb0NCYqyFCjKlKbMKt2nPP9qu4KG/XaBysTDwtG25nQWmszuVz1REFaiQ8RlMXE2TKaVTgBdkd2OLTkD75Fmq3zK/yQfCgrWcQ0i39aBG90PO9aTywIohf55qCureztVRpDZ94VSKEWXc8RivXJ/qK9XI9Dy8po8KXwDMPxWUQn/vBq+HnylWSQvRRvvzRw7rtSqMNX1Pyld0ZwVB8I2Nns4bv3LwC5TSUkxXX3POEoh0UJ2yacx6PsOpi21vVqBduIyqmb7wN6W+CIjOSoF93o3nlIXYZqVilVUxT8PTm3B0KoNUrQ+mbh5k+BHkKrSR+O/Mp8AuHWa+Uldu0Oa3G2eXKWM6t6RnlMZvMVB83i3YBfWuB2RieNFpnz40D92mhf+m+p6YM9LbJe8O1RzAkae861Ev5SKrQ+w3UWEHGZpUVEtc4d/NhRbaSE+e7sQKQvgMsfFyxWByrkT5vUos7gmeP9T0waiyLhLrmddwa5XKuXHu6WiOxRpP5sTxJk7tAicWbgZ2UtHhCeDPaosK0thNCIeQsyTXok0f8LKvGbsMvnVUG23Q9im1uIcoP9jj38CvW2Z5Hpqxe2dIUsuSREfV88CpBx6Fj6ePqEznuTF7CkD6mD7VsSKMcZ68I/v5Zd3CNszcfQCfrGj17voxaJvUAFKvhN2dpjpoUeQKUyYbw0doh4CPqBpTIcIM+cO+uO0DDg8W7be4XIly8I6t7Fb29C71one9PE0E3+/QHoP1Waq5r7MudxWqcDWDEIN9Ni2xglIbxXWZBEl5kXBPo26+5870OlESOys4orATyDuds6i1zqpbZ3LiEc6ogQIjuMnKTPr8o/t0KivGA+SAtXv7Sg3KLnWsJqju5i3WngDYvhW7b0EBcIfzX28DzEP/CQM+bCSPr1NcUFni9QyFCeSpKyVVZzWNBc36Kh4SyO5mQQ0Sjml7e4KK7MOgeP8RZySxztucLK1mWeIy/GCozJBGSZXuB9/rZ11v4e/rhg28Kfe0M2tnORKKcLqQTjW1i2N7sHxn0+4W0nPL7/aF0c0dQJc3D382CBZ/tJEjX9/ehLoA1EiYGqC8F+1eKzMkpIrD8N/idm4XKvhvuhZ0Nk1c3SLSGm6NhsFIsw5+z8KsyT73ZtnUYuMTO1oWVwqZB0aR2IhJBa90twvqcjb1kU9S+efRK85XrL9sR0nAbSkE2CRZG9hW3PY6IVHoQP/NWwvKgt6Rhg42DVqWTFnRmS6vFYXinr2uo2ELTNGdouaE4NOavSm6PAPj5dKmZsAkSKmXlcpRTryOjhzs1at48KqUtsEQQyM3+PD4+lH02Mx70i9NeE7n205S4O9M8s2/QEAPHDbehD7gXxapNCyilPdEGPVhw41tuudbyds27bxLXrP6dgSksk/kpkWcVtX92vVqtrq8fMCa0h9a6Ub6Hv+XAwI/buzjC84WNY2gCVzK5Wm2+hAa1zGAEzJ5tDEaOIh4EYDVPTRp/EifElVLYLXllX4AXS75vz+jL0xRNca8u08d6G2mIMLoJ4b1BYM6XcKPA4OC7j3b0iL6d55uGcZwcTxF8JJKCiPgJf3xk1+HKxSM8WAQ977PDk323Luoz3sYj0thdaPSMGqqg+G8vtbQCktkkWnQUWm5BJumJ+67ectlDde9HgyJb6eOcmtFO+kw3N0qhxTUxVuh7iJx0yltq60HVnlXThUIMoyDzjQ1f2Yp7KDYY68hBCf/YBE9LZDi6f/oG15FNMPRmrRT2GcWd2unD18AP4z4oIUsHp+tuRhx27vwMYz7yvhcthWaM1uwinB2+dXpwcLrt9vmwQiy9ybnELy+oG0gKW+kbePVgcGJg/jJ9IIGK2iL+HlIApCt4YFtN4lo3GOlF8aUpf3LLgr13yOps+CbwWJu1EstZAxq+aDafz2e0MMeRdq1yqs3GnoTk26YyitxsePbO8pK7AFLKc5Sz07xi0T6/dg5f7jikMTkFg27JSiqBDVQWiP64Jx7a7gZ2Z/QN9iVEKAd9l4xZKDE8CTGM7mBNmMBKV3A0If0dzWVNDnS7CtYWzXbZyBkaTsnqLPgL3K2TuZXE85naaNagcaVey1R3C1uzZHXo5C7K8NNV1+o/++n2tAYTWSqXp6jS/HLcle7g3KXqFHTeMKrptwBAm9JB+ijf6IvxF54DojMrZ/vnmOhhRLzEhvB3A/oxTvsvsoBByfTuYxUayaDDxstelA6AkLISspw8l6iJSbxbVKf0vdo58pHPhtIj8bmDtc3NzaODA+u/g8dGePTEeloRBFGPjU3S+LrJZ3dOaiRNQ/q4UpkcfY0tELN+kTxs5k4VIvIA1RwQfdquIn/rjs/A2Hq7g2EF8yWu7YyOIHrVSsyb2/HLr9C7GD3ZhA4IwrpB+v4B39qbx2IJdiFLktpcp/Sl1qrbT6AfCGvQ+OHN0E/XjkmO1JZ1cKs+/7JgiQKTrrglUWgC37zOkaU8mRurc7RveFsghFOHvFic8jl34oSf2YjitEHa2AV4nhWXCMs7zZLBdTAfGzD+pDO4XBUsJDxb5x+ZxMWwnsz0AkE5qtVq3/mJFEw4LMBAbeb14VptWGc7pe/nqrP8zXZeM7gmfFp2wxqfKtbsHa8KIH7zyvZ6X47frNVq5cWjOtRoLjsMAsHxXc3dIQfCTeXWx1M8zNA4TJ9kbTErtjeuldtZN7iO6Htko2nE0v9htRYWvWph6r+T8LCmfd8j6Zs1DGPYTyhAkCxVUlUkfYaR7Vz6Tn/O++6/+UbfrY1mspqTzY5O7versvXTq5pzJMIYBrePCckjb3qSeza9vVgs5cq4F83InKrBQD8UX47MjY7mYOhtjPYLhDKXJWkK0scDudC336gWrs0uUVS4I/qe3sHwbmGrejcPVlbdw097RR+0JgN+fP+9ONQkEdIHzXsXyls/uT3KGc9OvhkRVbF/RRUl8UXptS8AAAiOSURBVHlCPjbsOjmsEqmTTDSa3ZZQXrbj1eV9x2WDchrt30atgJ6dXJtSAyl1aq12ahJ+axZv/BKNKzH5iSUMcK7RO8Wum+6IPiuCd7EUY1j+ef0h+j8rq358WO0VfTBZxfSxZ/RRXdAX7B8G4FQjOU6rbp4uLy+frpWzYWj7jgztORH8LspBC0Q+ChDjJfp4B09P0qiBnsvfLbq1Zs743xM/3/QGML1Vy6TbuKEtbiXRprvD8FentnPsdU1X1ZvTcaUxWWR5MQ1282rCNSas1RvP+870EWImp4vxw0yL8TOg7YPRymuJ2MtyBlRCKpoM+rfD3LPavo10EAYuXK2cHyu7TQZ0tt6S4YgzthvoREt6AfdVsMOcAfXWK3Zp05ap3BiUNu8XHErEG2EOTH89uQ226VnoHr2gLzSkaQdxRVnYGPh6MpPJTH799XC/KUxp0QQhrNF0tQ4NG10VCQsV65b2oQmEYbNRXa3CdGu1MYOQOfFqwMqcF91R2Rkwt+/q2Pf22sYzr9+82q8qQuTGxkO/3PhCInLC5UrQk41rCnV1d9ur4NLHvRN9hLnj+LQhS4BGJWCKogAtS1AYKfvKKpp3pozig7GyoQE2hS0YubSTz+VKxcWxKo1aScdKblMVOYzaGP1g2q15haNrKpghs261/yU0em7JJrOsKkqgk67NM/UMioWCbMmFwlmbkST3ImnDnpf0XaCvq7iPCKi3x6oGF51cW55TxUhAVKeWN2vRGveICE0ZlDE/3zc2v0ruBthXrvz4Zo9W79adfBX7g1xx3mvpc/5mqfvuuiUV/WlI2XDCNKIvpd+d9Xl6uzwnKFJnpVyzdTk1pMTNVn3vTaMfjFYOpqenj87Rp+5PT+8vdEofbzIna282MqiLRCvlYexRQnW/ap577C5g2rWJYjVPjwpsbN2tTNF2MU9yue89vcVtpNglDFe9Tqxcf7wftehSWSEYf51c5txi4LElQr3tUG74wtX62YuCFYFvPhwJQODFbgKt2EJbE0RH/BdLBsCE8WubtwgxavLV21++2hietD3n4WQnJ09t54QwMz7Kse0HY6t5LiMQlrXidvBxdY569sp6ZXtTz+Uimj310VXb7UF4K05963Jb0pNbioBLBuToFDR6bbutQ/CrVuIXlwjVqztxQS9mLnkxCdNbF8m0LKcT+H8eCuf5Mwv+kXYfGmBUfaa28euvv6483SnuzM/v7LyZkwKnTnYPbVFE2auLqzb0vpA+Jq6om1m0iVCdokvzW5Z8y50/ILWXRWhwadRZHzb2VWvGa+Yw6vdUHpcM6Cw2eu1XUVmQDG5dDuQGrwpOhJs3EOsAEUtxt24VBNWa86B7RwSJufzp5uvbGK/PtioNMAyYmSnV/v3rn//867/6p/rn5vr7h1bWPPp8Rr2IfAOmj1EUxdqIklydpvJlevLN3uuqtyNsfqzuUHmbjs7q4oHjrajnV/G9caSNsLZhwVO6sEIBvLO5fUUIHLjifumpRE/2R4g0dw8hGFwFQ7jbfNo8R580zsdNNuXhzHqjZHnql5XR/P2vfoEMNjBjG9tIeX1c7R62dxmBtQRJUQRRzxt1Y3Rnk6OdSTl5J+PWAJ3aWLVcKvWDf5Yafflr6zkczQQ21vvbGb1Q42yCispbbagS24YnkR51mYaa9Jn6mwZuqw2rep6+PQBlr92boFrDyq+/bAzYz36aWVn56pdffnmxMnMnDz2vgMacnUU0pOuDrkP3s3jjEnXl0S3L2uSg0GXvxKxhDbdJ+uz6vWXR+tb1vZy2ubnkwyWDkHVyldFrnIMsEqDNrdxZNXaZ1FSa6c24agSEvPvFndi5Bko11b2THN5g7gxos7R2lgd6XobRD36FBJbzjmE48C0Mg8ygwMU/ZaDejTokKnoQ4ZPwLfgAWgwFihJ3K/Bk/uncdtlt1/DZq4cNo7f/9D6KXyB96mtwY6THe/8uQahcWLEOMpUe9VjxoJBuINmKxrFKO+8ebCyKNE43pDKMCoaQ5v5ycHB4+Pbt28PDg4N9chKKhEb56NwD6GG1OFQl3EDll/Bysvo66+35MLy3l85gE8jVHK/Nfmcab5QYBUJSNgWpzbIsf/E8rrhIq2BJAbwvN+9PSSDWeQPADeBVoF4LuR19QPfQlM0A7k6Q+7/65c8tmMnCpE1agySQ9RIV3hCIGPCcEdZgQZWHs27NJVt+nlyGMY6PrqGNcMjS2uwzd6BVG5TjQvtIT2ych3qDKqZUXdateDxu6bJ8bQtelwgFbkC70274auEsrIlg/gDQV1ZWfoFSCK3fyspJldsWCB3tR2KQXFYnhBgUU/dFfAQLYHx72Iucs9vy0DAMvCF9nLO57GVodOYwLl6V3qYa59H2LM+BT0n4CxMCH/3Osm0RNJstMvrUXnIKm4CKE33OEqdoiwIq+xot5sGnG3aHdzUYFDOem60W1WKNrDlkbW3Wa8bQ1pgO09vPHilTbTKoMjgYjxWNyTgR1Nc1bX+PJ4CMn2u+AptAQZF3sl7gMjwkb9draxuu5/VFp/X2Ru/3iZQgNhnEaYycHtY2oRc3VdVkCZDGz7Q4c7ZhAr92G5/pzPJJZbOxIpKZUq8wer9X8KGUoKDJbtWSdR0ARq+PHrmzACE96RJ7znLzKVeDm3Nt5XWvk2j0AGZoXQ4T/34QceVQBSdPi5WkpcduW8xF4cPg3Xt06z/jfay8YXxo9BYURfqjkkegGmDDDFpAly3G+7XNTtUhrMFKbBMSiEsGlDarK0KHNb3fK1ItnqT50GznCHhsAhXmZNLhqiXOyOBa/B/J6LWDX2AuQL3Klrk+2Iw/zlTt7AbzBzZ65xBB+4S48qeq101RE0HPBC7ugD+20bsAP74XVCByY/jmBTHiH93o/VbwKUzgH97o/WbAIOaPkaF9wRd8wRd8wvj/S07sqY0Ni7IAAAAASUVORK5CYII=')

col1, col2 = st.columns(2)
initial_amount = col1.number_input('Insert initial amount', 0, 1000000)
years_maintenance = col2.slider('Years of maintenance', 0, 25)



if initial_amount < 5000:
    list_etf = ['^GSPC']
elif initial_amount < 10000:
    list_etf = ['^GSPC', 'GC=F']
elif initial_amount < 25000:
    list_etf = ['^GSPC', 'GC=F', '^IXIC', '^TNX']
elif initial_amount < 50000:
    list_etf = ['^GSPC', 'GC=F', '^IXIC', '^TNX', '^FTSE', '^N225', '^GDAXI', '^FCHI','^STOXX50E'] # global indexes
else:
    list_etf = ['^GSPC', 'GC=F', '^IXIC', '^TNX', '^FTSE', '^N225', '^GDAXI', '^FCHI','^STOXX50E', 'EMQQ', 'FEM'] # emergents
    

start = "2012-06-30"
today = date.today().strftime("%Y-%m-%d")

list_etf_data = []
for i in range(len(list_etf)):
    print(i)
    etf = yf.download(list_etf[i], start, today)
    list_etf_data.append(etf)


# percentage of each investment

dict_initial_amount = {}
count = 0

if initial_amount < 5000: # only sp500
    investment1 = initial_amount/list_etf_data[count]['Adj Close'][-1]
    dict_initial_amount[list_etf[0]] = investment1

elif initial_amount < 10000: # Gold and sp
    investment1 = 0.8*initial_amount/list_etf_data[count]['Adj Close'][-1]
    count = count +1
    dict_initial_amount[list_etf[0]] = investment1
    investment2 = 0.2*initial_amount/list_etf_data[count]['Adj Close'][-1]
    dict_initial_amount[list_etf[1]] = investment2
    
elif initial_amount < 25000: # Gold, nq and sp
    investment1 = 0.4*initial_amount/list_etf_data[count]['Adj Close'][-1]
    dict_initial_amount[list_etf[0]] = investment1
    count = count +1
    
    investment2 = 0.2*initial_amount/list_etf_data[count]['Adj Close'][-1]
    dict_initial_amount[list_etf[1]] = investment2
    count = count +1
    
    investment3 = 0.2*initial_amount/list_etf_data[count]['Adj Close'][-1]
    dict_initial_amount[list_etf[2]] = investment3
    count = count +1
    
    investment4 = 0.2*initial_amount/list_etf_data[count]['Adj Close'][-1]
    dict_initial_amount[list_etf[3]] = investment4
    
elif initial_amount < 50000: # Gold, nq and sp
    investment1 = 0.2*initial_amount/list_etf_data[count]['Adj Close'][-1]
    dict_initial_amount[list_etf[0]] = investment1
    count = count +1
    
    investment2 = 0.1*initial_amount/list_etf_data[count]['Adj Close'].iloc[-1]
    dict_initial_amount[list_etf[1]] = investment2
    count = count +1
    
    investment3 = 0.1*initial_amount/list_etf_data[count]['Adj Close'].iloc[-1]
    dict_initial_amount[list_etf[2]] = investment3
    count = count +1
    
    investment4 = 0.1*initial_amount/list_etf_data[count]['Adj Close'].iloc[-1]
    dict_initial_amount[list_etf[3]] = investment4
    count = count +1
    
    investment5 = 0.1*initial_amount/list_etf_data[count]['Adj Close'].iloc[-1]
    dict_initial_amount[list_etf[4]] = investment5
    count = count +1
    
    investment6 = 0.1*initial_amount/list_etf_data[count]['Adj Close'].iloc[-1]
    dict_initial_amount[list_etf[5]] = investment6
    count = count +1
    
    investment7 = 0.1*initial_amount/list_etf_data[count]['Adj Close'].iloc[-1]
    dict_initial_amount[list_etf[6]] = investment7
    count = count +1
    
    investment8 = 0.1*initial_amount/list_etf_data[count]['Adj Close'].iloc[-1]
    dict_initial_amount[list_etf[7]] = investment8
    count = count +1
    
    investment9 = 0.1*initial_amount/list_etf_data[count]['Adj Close'].iloc[-1]
    dict_initial_amount[list_etf[8]] = investment9
    
else: # Gold, nq and sp
    investment1 = 0.2*initial_amount/list_etf_data[count]['Adj Close'].iloc[-1]
    dict_initial_amount[list_etf[0]] = investment1
    count = count +1
    
    investment2 = 0.1*initial_amount/list_etf_data[count]['Adj Close'].iloc[-1]
    dict_initial_amount[list_etf[1]] = investment2
    count = count +1
    
    investment3 = 0.1*initial_amount/list_etf_data[count]['Adj Close'].iloc[-1]
    dict_initial_amount[list_etf[2]] = investment3
    count = count +1
    
    investment4 = 0.08*initial_amount/list_etf_data[count]['Adj Close'].iloc[-1]
    dict_initial_amount[list_etf[3]] = investment4
    count = count +1
    
    investment5 = 0.08*initial_amount/list_etf_data[count]['Adj Close'].iloc[-1]
    dict_initial_amount[list_etf[4]] = investment5
    count = count +1
    
    investment6 = 0.08*initial_amount/list_etf_data[count]['Adj Close'].iloc[-1]
    dict_initial_amount[list_etf[5]] = investment6
    count = count +1
    
    investment7 = 0.08*initial_amount/list_etf_data[count]['Adj Close'].iloc[-1]
    dict_initial_amount[list_etf[6]] = investment7
    count = count +1
    
    investment8 = 0.08*initial_amount/list_etf_data[count]['Adj Close'].iloc[-1]
    dict_initial_amount[list_etf[7]] = investment8
    count = count +1
    
    investment9 = 0.08*initial_amount/list_etf_data[count]['Adj Close'].iloc[-1]
    dict_initial_amount[list_etf[8]] = investment9
    count = count +1
    
    investment10 = 0.06*initial_amount/list_etf_data[count]['Adj Close'].iloc[-1]
    dict_initial_amount[list_etf[9]] = investment10
    count = count +1
    
    investment11 = 0.06*initial_amount/list_etf_data[count]['Adj Close'].iloc[-1]
    dict_initial_amount[list_etf[10]] = investment11


def add_features(df):
    df = df.reset_index()
    df['HL_pct'] = (df['High'] - df['Low']) / df['Low']
    df['pct_change'] = (df['Close'] - df['Open']) / df['Open']
    df['Date'] = pd.to_datetime(df['Date'])
    df['year'] = df['Date'].dt.year
    df['month'] = df['Date'].dt.month
    df['day'] = df['Date'].dt.day
    df['day_of_week'] = df['Date'].dt.dayofweek

    day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    df['day_of_week'] = df['day_of_week'].map(lambda x: day_names[x])
    return df

for i in range(len(list_etf_data)):
    list_etf_data[i] = add_features(list_etf_data[i])


list_etf_data_years = {}

for i in range(len(list_etf_data)):
    years = list_etf_data[i]['year'].unique()
    list_values = []
    for j in range(len(years)):
        x = list_etf_data[i][list_etf_data[i]['year']==years[j]]
        list_values.append(x)
        if j == len(years)-1:
            list_etf_data_years[list_etf[i]] = list_values
        
        
list_etf_data_years_std = {}

for i in range(len(list_etf_data_years)):
    list_values = []
    for j in range(len(list_etf_data_years[list_etf[i]])):  # keys
        x = list_etf_data_years[list_etf[i]][j].describe()['pct_change'].loc['std']
        print(x)
        if x == np.float64('Nan'):
            print(x == np.float64('Nan'))
            x = list_etf_data_years[list_etf[i]][j].describe()['pct_change'].iloc[6]
        x = np.mean(x)
        list_values.append(x)
        if j == len(list_etf_data_years[list_etf[i]])-1:
            list_etf_data_years_std[list_etf[i]] = x
        

pct_by_years = {}
for i in range(len(list_etf_data_years)): # dict
    list_values = []
    for j in range(len(list_etf_data_years[list_etf[i]])):  # keys
            x = float(list_etf_data_years[list_etf[i]][j][-1:]['Close'])/float(list_etf_data_years[list_etf[i]][j][:1]['Close'])
            list_values.append(x)
            if j == len(list_etf_data_years[list_etf[i]])-1:
                pct_by_years[list_etf[i]] = list_values 
            

pct_by_active = {}

for i in range(len(pct_by_years)):
    list_values = []
    for j in range(len(pct_by_years[list_etf[i]])):
        x = pct_by_years[list_etf[i]][j]
        list_values.append(x)
        if j == len(pct_by_years[list_etf[i]])-1:
            pct_by_active[list_etf[i]] = statistics.mean(list_values)
            
            
dict_investments = {}
dict_all_values_investments = {}
for i in range(len(list_etf)):
    x = list_etf_data[i]['Adj Close'].iloc[-1]
    list_values = []
    for j in range(years_maintenance):
        x = x*pct_by_active[list_etf[i]]
        list_values.append(x)
        dict_investments[list_etf[i]] = x
        if j == years_maintenance-1:
            dict_all_values_investments[list_etf[i]] = list_values

final_amount ={}

for i in range(len(list_etf)):
    final_amount[list_etf[i]] = dict_initial_amount[list_etf[i]]*dict_investments[list_etf[i]]


final_total = []
for i in range(len(list_etf)):
    final_total.append(final_amount[list_etf[i]])
    
final_total = sum(final_total)


df_final = pd.DataFrame(dict_all_values_investments)


def standard_plus(price, st):
    x = price*st
    x = price + x
    return x

def standard_minus(price, st):
    x = price*st
    x = price - x
    return x

string_std = '_std_u' # % up
string_std_ = '_std_d' # down
# string_std_value = '_std_plus_value' # value
# string_std_value_ = '_std_minus_value'


for i in range(len(list_etf)):
    df_final[f'{list_etf[i]}{string_std}'] = list_etf_data_years_std[list_etf[i]]


df_final_std = df_final



for i in range(len(list_etf)):
    df_final_std[f'{list_etf[i]}{string_std}'] = df_final.apply(lambda x: standard_plus(x[list_etf[i]],
                                                                                    list_etf_data_years_std[list_etf[i]]),
                                                           axis=1)
    df_final_std[f'{list_etf[i]}{string_std_}'] = df_final.apply(lambda x: standard_minus(x[list_etf[i]],
                                                                                      list_etf_data_years_std[list_etf[i]]),
                                                            axis=1)


cols = []
for i in range(len(list_etf)):
    cols.append(df_final_std.columns[i+len(list_etf)])
    cols.append(df_final_std.columns[i])
    cols.append(df_final_std.columns[i+len(list_etf)*2])


df_final_std = df_final[cols]


df_final_std_invest = df_final_std

count = 0
for i in range(len(list_etf)):
    #i = i*3 # 012,345,678
    df_final_std_invest[df_final_std_invest.columns[count]] = df_final_std_invest[df_final_std_invest.columns[count]]*dict_initial_amount[list_etf[i]]
    df_final_std_invest[df_final_std_invest.columns[count+1]] = df_final_std_invest[df_final_std_invest.columns[count+1]]*dict_initial_amount[list_etf[i]]
    df_final_std_invest[df_final_std_invest.columns[count+2]] = df_final_std_invest[df_final_std_invest.columns[count+2]]*dict_initial_amount[list_etf[i]]
    count = count + 3 # columns of value an std


df_final_std_invest_plot = df_final_std_invest[list_etf]


list_final_invest = []

for i in range(len(df_final_std_invest_plot)):
    list_final_invest.append(df_final_std_invest_plot.iloc[i].sum())

final_result_invest_by_year = pd.DataFrame(list_final_invest)




tab1, tab2, tab3, tab4, tab5 = st.tabs(['Result chart', 'Tickers chart', 'Final result', 'Results', 'Tickers name'])
tab1.line_chart(final_result_invest_by_year)
tab2.line_chart(df_final_std_invest_plot)
tab3.table(final_result_invest_by_year)
tab4.table(df_final_std_invest)
tab5.markdown('Tickers')

st.markdown('DISCLAIMER')