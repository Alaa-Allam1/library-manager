owner_book = []
wish_list = []

book_1 = input ("Enter the name of a book you own: ")
owner_book.append (book_1)

book_2 = input("Enter the name of another book you own (or press 'Enter' to skip): ")
if book_2:
    owner_book.append (book_2)

print(f"\nYour library: {owner_book} \n")

Future_book_1 = input("Enter the name of a book you wish to have in the future: \n")
wish_list.append (Future_book_1)

Future_book_2 = input("Enter the name of another book you wish to have (or press 'Enter' to skip): ")
if Future_book_2:
    wish_list.append (Future_book_2)

print(f"\nYour Wishlist: {wish_list} \n")

have_book = input("Enter the name of a book from your wishlist that you have acquired (or press 'Enter' to skip):")
if have_book in wish_list:
    owner_book.append (have_book)
    wish_list.remove (have_book)

print(f"\nUpdated Library: {owner_book}")
print(f"Updated Wishlist: {wish_list} \n")

donated_book = input("Enter the name of a book from your library you wish to donate (or press 'Enter' to skip):")
if donated_book in owner_book:
    owner_book.remove (donated_book)

print(f"\nFinal Library after Donations: {owner_book}")
