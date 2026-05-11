





import java.util.List;
import java.util.ArrayList;

public class persistence_EntityFeature extends Feature, NamedDisplayElement {

    private String columnName;
    private String singletonName;
    private boolean unique;
    private String pluralisedName;
    private boolean ordered;
    private String booleanIsHasChoice;
    private String cardinality;



    public persistence_EntityFeature(
        String columnName,        String singletonName,        boolean unique,        String pluralisedName,        boolean ordered,        String booleanIsHasChoice,        String cardinality    ) {
        super(
        );
        this.columnName = columnName;
        this.singletonName = singletonName;
        this.unique = unique;
        this.pluralisedName = pluralisedName;
        this.ordered = ordered;
        this.booleanIsHasChoice = booleanIsHasChoice;
        this.cardinality = cardinality;
    }


    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
    }
    public String getSingletonname() {
        return singletonName;
    }

    public void setSingletonname(String singletonName) {
        this.singletonName = singletonName;
    }
    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }
    public String getPluralisedname() {
        return pluralisedName;
    }

    public void setPluralisedname(String pluralisedName) {
        this.pluralisedName = pluralisedName;
    }
    public boolean getOrdered() {
        return ordered;
    }

    public void setOrdered(boolean ordered) {
        this.ordered = ordered;
    }
    public String getBooleanishaschoice() {
        return booleanIsHasChoice;
    }

    public void setBooleanishaschoice(String booleanIsHasChoice) {
        this.booleanIsHasChoice = booleanIsHasChoice;
    }
    public String getCardinality() {
        return cardinality;
    }

    public void setCardinality(String cardinality) {
        this.cardinality = cardinality;
    }


}