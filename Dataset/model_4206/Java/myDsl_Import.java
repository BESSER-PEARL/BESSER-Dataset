





import java.util.List;
import java.util.ArrayList;

public class myDsl_Import  {

    private String Import_type;
    private int import_num;





    private myDsl_Model mydsl_model;


    public myDsl_Import(
        String Import_type,        int import_num    ) {
        this.Import_type = Import_type;
        this.import_num = import_num;
    }


    public String getImport_type() {
        return Import_type;
    }

    public void setImport_type(String Import_type) {
        this.Import_type = Import_type;
    }
    public int getImport_num() {
        return import_num;
    }

    public void setImport_num(int import_num) {
        this.import_num = import_num;
    }

    public myDsl_Model getMydsl_model() {
        return mydsl_model;
    }

    public void setMydsl_model(myDsl_Model mydsl_model) {
        this.mydsl_model = mydsl_model;
    }

}