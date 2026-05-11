





import java.util.List;
import java.util.ArrayList;

public class persistence_Feature extends NamedDisplayElement {

    private String defaultDisplayValue;
    private boolean ordered;
    private String displayClass;
    private boolean encodeUriKey;
    private boolean customiseSet;
    private String emptyDisplayValue;
    private boolean derived;
    private boolean collectionOrmAllowAdd;
    private String cardinality;
    private String headerClass;
    private boolean primaryKey;
    private String singletonName;
    private String footerClass;
    private String pluralisedName;
    private String title;
    private String columnName;
    private String booleanIsHasChoice;
    private boolean collectionOrmAllowRemove;



    public persistence_Feature(
        String defaultDisplayValue,        boolean ordered,        String displayClass,        boolean encodeUriKey,        boolean customiseSet,        String emptyDisplayValue,        boolean derived,        boolean collectionOrmAllowAdd,        String cardinality,        String headerClass,        boolean primaryKey,        String singletonName,        String footerClass,        String pluralisedName,        String title,        String columnName,        String booleanIsHasChoice,        boolean collectionOrmAllowRemove    ) {
        super(
        );
        this.defaultDisplayValue = defaultDisplayValue;
        this.ordered = ordered;
        this.displayClass = displayClass;
        this.encodeUriKey = encodeUriKey;
        this.customiseSet = customiseSet;
        this.emptyDisplayValue = emptyDisplayValue;
        this.derived = derived;
        this.collectionOrmAllowAdd = collectionOrmAllowAdd;
        this.cardinality = cardinality;
        this.headerClass = headerClass;
        this.primaryKey = primaryKey;
        this.singletonName = singletonName;
        this.footerClass = footerClass;
        this.pluralisedName = pluralisedName;
        this.title = title;
        this.columnName = columnName;
        this.booleanIsHasChoice = booleanIsHasChoice;
        this.collectionOrmAllowRemove = collectionOrmAllowRemove;
    }


    public String getDefaultdisplayvalue() {
        return defaultDisplayValue;
    }

    public void setDefaultdisplayvalue(String defaultDisplayValue) {
        this.defaultDisplayValue = defaultDisplayValue;
    }
    public boolean getOrdered() {
        return ordered;
    }

    public void setOrdered(boolean ordered) {
        this.ordered = ordered;
    }
    public String getDisplayclass() {
        return displayClass;
    }

    public void setDisplayclass(String displayClass) {
        this.displayClass = displayClass;
    }
    public boolean getEncodeurikey() {
        return encodeUriKey;
    }

    public void setEncodeurikey(boolean encodeUriKey) {
        this.encodeUriKey = encodeUriKey;
    }
    public boolean getCustomiseset() {
        return customiseSet;
    }

    public void setCustomiseset(boolean customiseSet) {
        this.customiseSet = customiseSet;
    }
    public String getEmptydisplayvalue() {
        return emptyDisplayValue;
    }

    public void setEmptydisplayvalue(String emptyDisplayValue) {
        this.emptyDisplayValue = emptyDisplayValue;
    }
    public boolean getDerived() {
        return derived;
    }

    public void setDerived(boolean derived) {
        this.derived = derived;
    }
    public boolean getCollectionormallowadd() {
        return collectionOrmAllowAdd;
    }

    public void setCollectionormallowadd(boolean collectionOrmAllowAdd) {
        this.collectionOrmAllowAdd = collectionOrmAllowAdd;
    }
    public String getCardinality() {
        return cardinality;
    }

    public void setCardinality(String cardinality) {
        this.cardinality = cardinality;
    }
    public String getHeaderclass() {
        return headerClass;
    }

    public void setHeaderclass(String headerClass) {
        this.headerClass = headerClass;
    }
    public boolean getPrimarykey() {
        return primaryKey;
    }

    public void setPrimarykey(boolean primaryKey) {
        this.primaryKey = primaryKey;
    }
    public String getSingletonname() {
        return singletonName;
    }

    public void setSingletonname(String singletonName) {
        this.singletonName = singletonName;
    }
    public String getFooterclass() {
        return footerClass;
    }

    public void setFooterclass(String footerClass) {
        this.footerClass = footerClass;
    }
    public String getPluralisedname() {
        return pluralisedName;
    }

    public void setPluralisedname(String pluralisedName) {
        this.pluralisedName = pluralisedName;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
    }
    public String getBooleanishaschoice() {
        return booleanIsHasChoice;
    }

    public void setBooleanishaschoice(String booleanIsHasChoice) {
        this.booleanIsHasChoice = booleanIsHasChoice;
    }
    public boolean getCollectionormallowremove() {
        return collectionOrmAllowRemove;
    }

    public void setCollectionormallowremove(boolean collectionOrmAllowRemove) {
        this.collectionOrmAllowRemove = collectionOrmAllowRemove;
    }


}