





import java.util.List;
import java.util.ArrayList;

public class metamodel_Sequence  {

    private String name;
    private String maxValue;
    private int incrementby;
    private int minValue;
    private boolean cycle;
    private String currentValue;
    private String startwith;





    private metamodel_Database metamodel_database;


    public metamodel_Sequence(
        String name,        String maxValue,        int incrementby,        int minValue,        boolean cycle,        String currentValue,        String startwith    ) {
        this.name = name;
        this.maxValue = maxValue;
        this.incrementby = incrementby;
        this.minValue = minValue;
        this.cycle = cycle;
        this.currentValue = currentValue;
        this.startwith = startwith;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMaxvalue() {
        return maxValue;
    }

    public void setMaxvalue(String maxValue) {
        this.maxValue = maxValue;
    }
    public int getIncrementby() {
        return incrementby;
    }

    public void setIncrementby(int incrementby) {
        this.incrementby = incrementby;
    }
    public int getMinvalue() {
        return minValue;
    }

    public void setMinvalue(int minValue) {
        this.minValue = minValue;
    }
    public boolean getCycle() {
        return cycle;
    }

    public void setCycle(boolean cycle) {
        this.cycle = cycle;
    }
    public String getCurrentvalue() {
        return currentValue;
    }

    public void setCurrentvalue(String currentValue) {
        this.currentValue = currentValue;
    }
    public String getStartwith() {
        return startwith;
    }

    public void setStartwith(String startwith) {
        this.startwith = startwith;
    }

    public metamodel_Database getMetamodel_database() {
        return metamodel_database;
    }

    public void setMetamodel_database(metamodel_Database metamodel_database) {
        this.metamodel_database = metamodel_database;
    }

}