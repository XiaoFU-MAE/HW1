for $x in doc("Users/xiaofu/Desktop/Econ435/books.xml")//book
order by xs:float($x/price)descending, $x/title ascending
return $x


