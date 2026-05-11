





import java.util.List;
import java.util.ArrayList;

public class persistence_EntityFeature extends Feature, NamedDisplayElement {

    private String booleanIsHasChoice;
    private boolean ordered;
    private String pluralisedName;
    private String singletonName;
    private boolean derived;
    private boolean customiseSet;
    private boolean primaryKey;
    private String cardinality;
    private String columnName;



    public persistence_EntityFeature(
        String booleanIsHasChoice,        boolean ordered,        String pluralisedName,        String singletonName,        boolean derived,        boolean customiseSet,        boolean primaryKey,        String cardinality,        String columnName    ) {
        super(
        );
        this.booleanIsHasChoice = booleanIsHasChoice;
        this.ordered = ordered;
        this.pluralisedName = pluralisedName;
        this.singletonName = singletonName;
        this.derived = derived;
        this.customiseSet = customiseSet;
        this.primaryKey = primaryKey;
        this.cardinality = cardinality;
        this.columnName = columnName;
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
    public String getPluralisedname() {
        return pluralisedName;
    }

    public void setPluralisedname(String pluralisedName) {
        this.pluralisedName = pluralisedName;
    }
    public String getSingletonname() {
        return singletonName;
    }

    public void setSingletonname(String singletonName) {
        this.singletonName = singletonName;
    }
    public boolean getDerived() {
        return derived;
    }

    public void setDerived(boolean derived) {
        this.derived = derived;
    }
    public boolean getCustomiseset() {
        return customiseSet;
    }

    public void setCustomiseset(boolean customiseSet) {
        this.customiseSet = customiseSet;
    }
    public boolean getPrimarykey() {
        return primaryKey;
    }

    public void setPrimarykey(boolean primaryKey) {
        this.primaryKey = primaryKey;
    }
    public String getCardinality() {
        return cardinality;
    }

    public void setCardinality(String cardinality) {
        this.cardinality = cardinality;
    }
    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
    }


}