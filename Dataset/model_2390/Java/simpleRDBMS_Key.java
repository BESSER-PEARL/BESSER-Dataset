





import java.util.List;
import java.util.ArrayList;

public class simpleRDBMS_Key extends NamedElement {






    private simpleRDBMS_ForeignKey simplerdbms_foreignkey;




    private simpleRDBMS_Table simplerdbms_table;


    public simpleRDBMS_Key(
    ) {
        super(
        );
    }



    public simpleRDBMS_ForeignKey getSimplerdbms_foreignkey() {
        return simplerdbms_foreignkey;
    }

    public void setSimplerdbms_foreignkey(simpleRDBMS_ForeignKey simplerdbms_foreignkey) {
        this.simplerdbms_foreignkey = simplerdbms_foreignkey;
    }
    public simpleRDBMS_Table getSimplerdbms_table() {
        return simplerdbms_table;
    }

    public void setSimplerdbms_table(simpleRDBMS_Table simplerdbms_table) {
        this.simplerdbms_table = simplerdbms_table;
    }

}