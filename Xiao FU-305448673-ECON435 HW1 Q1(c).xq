 
for $value in distinct-values(doc("books.xml")/catalog/book/author )

let $count := count(doc("books.xml")/catalog/book[author eq $value])
order by $count descending
return concat($value," ",$count)