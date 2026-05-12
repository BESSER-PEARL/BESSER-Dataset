





import java.util.List;
import java.util.ArrayList;

public class Management  {

    private String specialoffers;
    private String suggetions;





    private Property property;


    public Management(
        String specialoffers,        String suggetions    ) {
        this.specialoffers = specialoffers;
        this.suggetions = suggetions;
    }


    public String getSpecialoffers() {
        return specialoffers;
    }

    public void setSpecialoffers(String specialoffers) {
        this.specialoffers = specialoffers;
    }
    public String getSuggetions() {
        return suggetions;
    }

    public void setSuggetions(String suggetions) {
        this.suggetions = suggetions;
    }

    public Property getProperty() {
        return property;
    }

    public void setProperty(Property property) {
        this.property = property;
    }

}