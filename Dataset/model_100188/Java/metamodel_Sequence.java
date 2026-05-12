





import java.util.List;
import java.util.ArrayList;

public class metamodel_Sequence  {

    private int minValue;
    private String currentValue;
    private String name;
    private boolean cycle;
    private String startwith;
    private String maxValue;
    private int incrementby;





    private metamodel_Database metamodel_database;


    public metamodel_Sequence(
        int minValue,        String currentValue,        String name,        boolean cycle,        String startwith,        String maxValue,        int incrementby    ) {
        this.minValue = minValue;
        this.currentValue = currentValue;
        this.name = name;
        this.cycle = cycle;
        this.startwith = startwith;
        this.maxValue = maxValue;
        this.incrementby = incrementby;
    }


    public int getMinvalue() {
        return minValue;
    }

    public void setMinvalue(int minValue) {
        this.minValue = minValue;
    }
    public String getCurrentvalue() {
        return currentValue;
    }

    public void setCurrentvalue(String currentValue) {
        this.currentValue = currentValue;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getCycle() {
        return cycle;
    }

    public void setCycle(boolean cycle) {
        this.cycle = cycle;
    }
    public String getStartwith() {
        return startwith;
    }

    public void setStartwith(String startwith) {
        this.startwith = startwith;
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

    public metamodel_Database getMetamodel_database() {
        return metamodel_database;
    }

    public void setMetamodel_database(metamodel_Database metamodel_database) {
        this.metamodel_database = metamodel_database;
    }

}