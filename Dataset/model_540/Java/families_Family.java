





import java.util.List;
import java.util.ArrayList;

public class families_Family extends NamedElement {

    private String id;
    private int lotteryNumbers;
    private String address;
    private float averageAge;
    private int numberOfChildren;
    private float averageAgePrecise;
    private boolean nuclear;



    public families_Family(
        String id,        int lotteryNumbers,        String address,        float averageAge,        int numberOfChildren,        float averageAgePrecise,        boolean nuclear    ) {
        super(
        );
        this.id = id;
        this.lotteryNumbers = lotteryNumbers;
        this.address = address;
        this.averageAge = averageAge;
        this.numberOfChildren = numberOfChildren;
        this.averageAgePrecise = averageAgePrecise;
        this.nuclear = nuclear;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public int getLotterynumbers() {
        return lotteryNumbers;
    }

    public void setLotterynumbers(int lotteryNumbers) {
        this.lotteryNumbers = lotteryNumbers;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public float getAverageage() {
        return averageAge;
    }

    public void setAverageage(float averageAge) {
        this.averageAge = averageAge;
    }
    public int getNumberofchildren() {
        return numberOfChildren;
    }

    public void setNumberofchildren(int numberOfChildren) {
        this.numberOfChildren = numberOfChildren;
    }
    public float getAverageageprecise() {
        return averageAgePrecise;
    }

    public void setAverageageprecise(float averageAgePrecise) {
        this.averageAgePrecise = averageAgePrecise;
    }
    public boolean getNuclear() {
        return nuclear;
    }

    public void setNuclear(boolean nuclear) {
        this.nuclear = nuclear;
    }


}