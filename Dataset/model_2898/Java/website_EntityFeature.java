





import java.util.List;
import java.util.ArrayList;

public class website_EntityFeature extends Feature, NamedDisplayElement {

    private String columnName;
    private String pluralisedName;
    private boolean unique;
    private String booleanIsHasChoice;
    private boolean ordered;
    private String cardinality;
    private String singletonName;



    public website_EntityFeature(
        String columnName,        String pluralisedName,        boolean unique,        String booleanIsHasChoice,        boolean ordered,        String cardinality,        String singletonName    ) {
        super(
        );
        this.columnName = columnName;
        this.pluralisedName = pluralisedName;
        this.unique = unique;
        this.booleanIsHasChoice = booleanIsHasChoice;
        this.ordered = ordered;
        this.cardinality = cardinality;
        this.singletonName = singletonName;
    }


    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
    }
    public String getPluralisedname() {
        return pluralisedName;
    }

    public void setPluralisedname(String pluralisedName) {
        this.pluralisedName = pluralisedName;
    }
    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }
    public String getBooleanishaschoice() {
        return booleanIsHasChoice;
    }

    public void setBooleanishaschoice(String booleanIsHasChoice) {
        this.booleanIsHasChoice = booleanIsHasChoice;
    }
    public boolean getOrdered() {
        return ordered;
    }

    public void setOrdered(boolean ordered) {
        this.ordered = ordered;
    }
    public String getCardinality() {
        return cardinality;
    }

    public void setCardinality(String cardinality) {
        this.cardinality = cardinality;
    }
    public String getSingletonname() {
        return singletonName;
    }

    public void setSingletonname(String singletonName) {
        this.singletonName = singletonName;
    }


}