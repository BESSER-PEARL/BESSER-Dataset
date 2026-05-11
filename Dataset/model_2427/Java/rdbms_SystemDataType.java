





import java.util.List;
import java.util.ArrayList;

public class rdbms_SystemDataType extends DataType {

    private int predefinedDecPlaces;
    private int predefinedLength;





    private rdbms_Database rdbms_database;




    private rdbms_UserDefinedDataType rdbms_userdefineddatatype;


    public rdbms_SystemDataType(
        int predefinedDecPlaces,        int predefinedLength    ) {
        super(
        );
        this.predefinedDecPlaces = predefinedDecPlaces;
        this.predefinedLength = predefinedLength;
    }


    public int getPredefineddecplaces() {
        return predefinedDecPlaces;
    }

    public void setPredefineddecplaces(int predefinedDecPlaces) {
        this.predefinedDecPlaces = predefinedDecPlaces;
    }
    public int getPredefinedlength() {
        return predefinedLength;
    }

    public void setPredefinedlength(int predefinedLength) {
        this.predefinedLength = predefinedLength;
    }

    public rdbms_Database getRdbms_database() {
        return rdbms_database;
    }

    public void setRdbms_database(rdbms_Database rdbms_database) {
        this.rdbms_database = rdbms_database;
    }
    public rdbms_UserDefinedDataType getRdbms_userdefineddatatype() {
        return rdbms_userdefineddatatype;
    }

    public void setRdbms_userdefineddatatype(rdbms_UserDefinedDataType rdbms_userdefineddatatype) {
        this.rdbms_userdefineddatatype = rdbms_userdefineddatatype;
    }

}