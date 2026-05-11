





import java.util.List;
import java.util.ArrayList;

public class DbMddAndroid_Relation  {

    private int minTargetMultiplicity;
    private int minSourceMultiplicity;
    private int maxSourceMultiplicity;
    private int maxTargetMultiplicity;





    private DbMddAndroid_DBScheme dbmddandroid_dbscheme;




    private DbMddAndroid_Table dbmddandroid_table;




    private DbMddAndroid_Table dbmddandroid_table;




    private DbMddAndroid_Table dbmddandroid_table;




    private DbMddAndroid_Table dbmddandroid_table;


    public DbMddAndroid_Relation(
        int minTargetMultiplicity,        int minSourceMultiplicity,        int maxSourceMultiplicity,        int maxTargetMultiplicity    ) {
        this.minTargetMultiplicity = minTargetMultiplicity;
        this.minSourceMultiplicity = minSourceMultiplicity;
        this.maxSourceMultiplicity = maxSourceMultiplicity;
        this.maxTargetMultiplicity = maxTargetMultiplicity;
    }


    public int getMintargetmultiplicity() {
        return minTargetMultiplicity;
    }

    public void setMintargetmultiplicity(int minTargetMultiplicity) {
        this.minTargetMultiplicity = minTargetMultiplicity;
    }
    public int getMinsourcemultiplicity() {
        return minSourceMultiplicity;
    }

    public void setMinsourcemultiplicity(int minSourceMultiplicity) {
        this.minSourceMultiplicity = minSourceMultiplicity;
    }
    public int getMaxsourcemultiplicity() {
        return maxSourceMultiplicity;
    }

    public void setMaxsourcemultiplicity(int maxSourceMultiplicity) {
        this.maxSourceMultiplicity = maxSourceMultiplicity;
    }
    public int getMaxtargetmultiplicity() {
        return maxTargetMultiplicity;
    }

    public void setMaxtargetmultiplicity(int maxTargetMultiplicity) {
        this.maxTargetMultiplicity = maxTargetMultiplicity;
    }

    public DbMddAndroid_DBScheme getDbmddandroid_dbscheme() {
        return dbmddandroid_dbscheme;
    }

    public void setDbmddandroid_dbscheme(DbMddAndroid_DBScheme dbmddandroid_dbscheme) {
        this.dbmddandroid_dbscheme = dbmddandroid_dbscheme;
    }
    public DbMddAndroid_Table getDbmddandroid_table() {
        return dbmddandroid_table;
    }

    public void setDbmddandroid_table(DbMddAndroid_Table dbmddandroid_table) {
        this.dbmddandroid_table = dbmddandroid_table;
    }
    public DbMddAndroid_Table getDbmddandroid_table() {
        return dbmddandroid_table;
    }

    public void setDbmddandroid_table(DbMddAndroid_Table dbmddandroid_table) {
        this.dbmddandroid_table = dbmddandroid_table;
    }
    public DbMddAndroid_Table getDbmddandroid_table() {
        return dbmddandroid_table;
    }

    public void setDbmddandroid_table(DbMddAndroid_Table dbmddandroid_table) {
        this.dbmddandroid_table = dbmddandroid_table;
    }
    public DbMddAndroid_Table getDbmddandroid_table() {
        return dbmddandroid_table;
    }

    public void setDbmddandroid_table(DbMddAndroid_Table dbmddandroid_table) {
        this.dbmddandroid_table = dbmddandroid_table;
    }

}