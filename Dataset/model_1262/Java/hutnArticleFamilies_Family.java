





import java.util.List;
import java.util.ArrayList;

public class hutnArticleFamilies_Family  {

    private String name;
    private boolean migrant;
    private boolean nuclear;
    private int lotteryNumbers;





    private hutnArticleFamilies_Family hutnarticlefamilies_family;


    public hutnArticleFamilies_Family(
        String name,        boolean migrant,        boolean nuclear,        int lotteryNumbers    ) {
        this.name = name;
        this.migrant = migrant;
        this.nuclear = nuclear;
        this.lotteryNumbers = lotteryNumbers;
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
    public boolean getNuclear() {
        return nuclear;
    }

    public void setNuclear(boolean nuclear) {
        this.nuclear = nuclear;
    }
    public int getLotterynumbers() {
        return lotteryNumbers;
    }

    public void setLotterynumbers(int lotteryNumbers) {
        this.lotteryNumbers = lotteryNumbers;
    }

    public hutnArticleFamilies_Family getHutnarticlefamilies_family() {
        return hutnarticlefamilies_family;
    }

    public void setHutnarticlefamilies_family(hutnArticleFamilies_Family hutnarticlefamilies_family) {
        this.hutnarticlefamilies_family = hutnarticlefamilies_family;
    }

}