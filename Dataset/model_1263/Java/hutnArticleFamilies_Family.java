





import java.util.List;
import java.util.ArrayList;

public class hutnArticleFamilies_Family  {

    private String name;
    private boolean migrant;
    private int lotteryNumbers;
    private boolean nuclear;





    private List<hutnArticleFamilies_Person> hutnarticlefamilies_persons;




    private hutnArticleFamilies_Family hutnarticlefamilies_family;


    public hutnArticleFamilies_Family(
        String name,        boolean migrant,        int lotteryNumbers,        boolean nuclear    ) {
        this.name = name;
        this.migrant = migrant;
        this.lotteryNumbers = lotteryNumbers;
        this.nuclear = nuclear;
        this.hutnarticlefamilies_persons = new ArrayList<>();
    }

    public hutnArticleFamilies_Family(
        String name,        boolean migrant,        int lotteryNumbers,        boolean nuclear        ArrayList<hutnArticleFamilies_Person> hutnarticlefamilies_persons    ) {
        this.name = name;
        this.migrant = migrant;
        this.lotteryNumbers = lotteryNumbers;
        this.nuclear = nuclear;
        this.hutnarticlefamilies_persons = hutnarticlefamilies_persons;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getMigrant() {
        return migrant;
    }

    public void setMigrant(boolean migrant) {
        this.migrant = migrant;
    }
    public int getLotterynumbers() {
        return lotteryNumbers;
    }

    public void setLotterynumbers(int lotteryNumbers) {
        this.lotteryNumbers = lotteryNumbers;
    }
    public boolean getNuclear() {
        return nuclear;
    }

    public void setNuclear(boolean nuclear) {
        this.nuclear = nuclear;
    }

    public List<hutnArticleFamilies_Person> getHutnarticlefamilies_persons() {
        return hutnarticlefamilies_persons;
    }

    public void addHutnarticlefamilies_person(Hutnarticlefamilies_person hutnarticlefamilies_person) {
        this.hutnarticlefamilies_persons.add(hutnarticlefamilies_person);
    }
    public hutnArticleFamilies_Family getHutnarticlefamilies_family() {
        return hutnarticlefamilies_family;
    }

    public void setHutnarticlefamilies_family(hutnArticleFamilies_Family hutnarticlefamilies_family) {
        this.hutnarticlefamilies_family = hutnarticlefamilies_family;
    }

}