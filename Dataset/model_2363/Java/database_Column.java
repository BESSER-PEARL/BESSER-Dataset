





import java.util.List;
import java.util.ArrayList;

public class database_Column extends NamedElement {

    private boolean unique;
    private String defaultValue;
    private boolean inForeignKey;
    private boolean autoincrement;
    private boolean inPrimaryKey;
    private boolean nullable;





    private database_Sequence database_sequence;




    private database_Sequence database_sequence;


    public database_Column(
        boolean unique,        String defaultValue,        boolean inForeignKey,        boolean autoincrement,        boolean inPrimaryKey,        boolean nullable    ) {
        super(
        );
        this.unique = unique;
        this.defaultValue = defaultValue;
        this.inForeignKey = inForeignKey;
        this.autoincrement = autoincrement;
        this.inPrimaryKey = inPrimaryKey;
        this.nullable = nullable;
    }


    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public boolean getInforeignkey() {
        return inForeignKey;
    }

    public void setInforeignkey(boolean inForeignKey) {
        this.inForeignKey = inForeignKey;
    }
    public boolean getAutoincrement() {
        return autoincrement;
    }

    public void setAutoincrement(boolean autoincrement) {
        this.autoincrement = autoincrement;
    }
    public boolean getInprimarykey() {
        return inPrimaryKey;
    }

    public void setInprimarykey(boolean inPrimaryKey) {
        this.inPrimaryKey = inPrimaryKey;
    }
    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }

    public database_Sequence getDatabase_sequence() {
        return database_sequence;
    }

    public void setDatabase_sequence(database_Sequence database_sequence) {
        this.database_sequence = database_sequence;
    }
    public database_Sequence getDatabase_sequence() {
        return database_sequence;
    }

    public void setDatabase_sequence(database_Sequence database_sequence) {
        this.database_sequence = database_sequence;
    }

}