calculate_age_bmi <- function(birth_year, height, weight) {
    # Calculate age
    current_year <- as.integer(format(Sys.Date(), "%Y"))
    age <- current_year - birth_year
    
    # Calculate BMI
    bmi <- weight / (height^2)
    
    # Return age and BMI
    return(list(age = age, bmi = bmi))
}