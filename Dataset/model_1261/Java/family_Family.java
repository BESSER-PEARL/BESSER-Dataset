





import java.util.List;
import java.util.ArrayList;

public class family_Family  {

    private String favoriteHolidayDestinations;
    private boolean hasASwimmingPool;
    private int numberOfPets;
    private String surname;





    private List<family_Person> family_persons;




    private family_Address family_address;


    public family_Family(
        String favoriteHolidayDestinations,        boolean hasASwimmingPool,        int numberOfPets,        String surname    ) {
        this.favoriteHolidayDestinations = favoriteHolidayDestinations;
        this.hasASwimmingPool = hasASwimmingPool;
        this.numberOfPets = numberOfPets;
        this.surname = surname;
        this.family_persons = new ArrayList<>();
    }

    public family_Family(
        String favoriteHolidayDestinations,        boolean hasASwimmingPool,        int numberOfPets,        String surname        ArrayList<family_Person> family_persons    ) {
        this.favoriteHolidayDestinations = favoriteHolidayDestinations;
        this.hasASwimmingPool = hasASwimmingPool;
        this.numberOfPets = numberOfPets;
        this.surname = surname;
        this.family_persons = family_persons;
    }

    public String getFavoriteholidaydestinations() {
        return favoriteHolidayDestinations;
    }

    public void setFavoriteholidaydestinations(String favoriteHolidayDestinations) {
        this.favoriteHolidayDestinations = favoriteHolidayDestinations;
    }
    public boolean getHasaswimmingpool() {
        return hasASwimmingPool;
    }

    public void setHasaswimmingpool(boolean hasASwimmingPool) {
        this.hasASwimmingPool = hasASwimmingPool;
    }
    public int getNumberofpets() {
        return numberOfPets;
    }

    public void setNumberofpets(int numberOfPets) {
        this.numberOfPets = numberOfPets;
    }
    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }

    public List<family_Person> getFamily_persons() {
        return family_persons;
    }

    public void addFamily_person(Family_person family_person) {
        this.family_persons.add(family_person);
    }
    public family_Address getFamily_address() {
        return family_address;
    }

    public void setFamily_address(family_Address family_address) {
        this.family_address = family_address;
    }

}