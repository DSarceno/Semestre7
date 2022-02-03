# PROGRAM probability
# random number generator with table format
data <- table(sample(1:2, 100, replace=TRUE))
for (x in 1:99){
data <- data + table(sample(1:2, 100, replace=TRUE))
}
print(data)

# file write
write.table(data, "datos.dat", row.names = F, col.names = F, quote = FALSE)
# END probability
