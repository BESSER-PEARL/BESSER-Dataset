





import java.util.List;
import java.util.ArrayList;

public class Management  {

    private String suggetions;
    private String specialoffers;





    private Property property;


    public Management(
        String suggetions,        String specialoffers    ) {
        this.suggetions = suggetions;
        this.specialoffers = specialoffers;
    }


    public String getSuggetions() {
        return suggetions;
    }

    public void setSuggetions(String suggetions) {
        this.suggetions = suggetions;
    }
    public String getSpecialoffers() {
        return specialoffers;
    }

    public void setSpecialoffers(String specialoffers) {
        this.specialoffers = specialoffers;
    }

    public Property getProperty() {
        return property;
    }

    public void setProperty(Property property) {
        this.property = property;
    }

}