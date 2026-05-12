





import java.util.List;
import java.util.ArrayList;

public class Table  {






    private SimpleRDBMS_Column simplerdbms_column;




    private SimpleRDBMS_Key simplerdbms_key;




    private SimpleRDBMS_Schema simplerdbms_schema;




    private SimpleRDBMS_ForeignKey simplerdbms_foreignkey;


    public Table(
    ) {
    }



    public SimpleRDBMS_Column getSimplerdbms_column() {
        return simplerdbms_column;
    }

    public void setSimplerdbms_column(SimpleRDBMS_Column simplerdbms_column) {
        this.simplerdbms_column = simplerdbms_column;
    }
    public SimpleRDBMS_Key getSimplerdbms_key() {
        return simplerdbms_key;
    }

    public void setSimplerdbms_key(SimpleRDBMS_Key simplerdbms_key) {
        this.simplerdbms_key = simplerdbms_key;
    }
    public SimpleRDBMS_Schema getSimplerdbms_schema() {
        return simplerdbms_schema;
    }

    public void setSimplerdbms_schema(SimpleRDBMS_Schema simplerdbms_schema) {
        this.simplerdbms_schema = simplerdbms_schema;
    }
    public SimpleRDBMS_ForeignKey getSimplerdbms_foreignkey() {
        return simplerdbms_foreignkey;
    }

    public void setSimplerdbms_foreignkey(SimpleRDBMS_ForeignKey simplerdbms_foreignkey) {
        this.simplerdbms_foreignkey = simplerdbms_foreignkey;
    }

}