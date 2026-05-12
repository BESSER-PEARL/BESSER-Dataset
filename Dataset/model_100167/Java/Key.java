





import java.util.List;
import java.util.ArrayList;

public class Key  {






    private SimpleRDBMS_Table simplerdbms_table;




    private SimpleRDBMS_ForeignKey simplerdbms_foreignkey;




    private SimpleRDBMS_Column simplerdbms_column;


    public Key(
    ) {
    }



    public SimpleRDBMS_Table getSimplerdbms_table() {
        return simplerdbms_table;
    }

    public void setSimplerdbms_table(SimpleRDBMS_Table simplerdbms_table) {
        this.simplerdbms_table = simplerdbms_table;
    }
    public SimpleRDBMS_ForeignKey getSimplerdbms_foreignkey() {
        return simplerdbms_foreignkey;
    }

    public void setSimplerdbms_foreignkey(SimpleRDBMS_ForeignKey simplerdbms_foreignkey) {
        this.simplerdbms_foreignkey = simplerdbms_foreignkey;
    }
    public SimpleRDBMS_Column getSimplerdbms_column() {
        return simplerdbms_column;
    }

    public void setSimplerdbms_column(SimpleRDBMS_Column simplerdbms_column) {
        this.simplerdbms_column = simplerdbms_column;
    }

}