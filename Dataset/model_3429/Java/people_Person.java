





import java.util.List;
import java.util.ArrayList;

public class people_Person  {

    private boolean alive;
    private String lotteryChances;
    private String name;
    private String nicknames;
    private int age;
    private int luckyNumbers;





    private people_Model people_model;




    private people_Person people_person;




    private List<people_Pet> people_pets;


    public people_Person(
        boolean alive,        String lotteryChances,        String name,        String nicknames,        int age,        int luckyNumbers    ) {
        this.alive = alive;
        this.lotteryChances = lotteryChances;
        this.name = name;
        this.nicknames = nicknames;
        this.age = age;
        this.luckyNumbers = luckyNumbers;
        this.people_pets = new ArrayList<>();
    }

    public people_Person(
        boolean alive,        String lotteryChances,        String name,        String nicknames,        int age,        int luckyNumbers        ArrayList<people_Pet> people_pets    ) {
        this.alive = alive;
        this.lotteryChances = lotteryChances;
        this.name = name;
        this.nicknames = nicknames;
        this.age = age;
        this.luckyNumbers = luckyNumbers;
        this.people_pets = people_pets;
    }

    public boolean getAlive() {
        return alive;
    }

    public void setAlive(boolean alive) {
        this.alive = alive;
    }
    public String getLotterychances() {
        return lotteryChances;
    }

    public void setLotterychances(String lotteryChances) {
        this.lotteryChances = lotteryChances;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getNicknames() {
        return nicknames;
    }

    public void setNicknames(String nicknames) {
        this.nicknames = nicknames;
    }
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
    public int getLuckynumbers() {
        return luckyNumbers;
    }

    public void setLuckynumbers(int luckyNumbers) {
        this.luckyNumbers = luckyNumbers;
    }

    public people_Model getPeople_model() {
        return people_model;
    }

    public void setPeople_model(people_Model people_model) {
        this.people_model = people_model;
    }
    public people_Person getPeople_person() {
        return people_person;
    }

    public void setPeople_person(people_Person people_person) {
        this.people_person = people_person;
    }
    public List<people_Pet> getPeople_pets() {
        return people_pets;
    }

    public void addPeople_pet(People_pet people_pet) {
        this.people_pets.add(people_pet);
    }

}