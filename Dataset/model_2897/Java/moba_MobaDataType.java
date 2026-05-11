





import java.util.List;
import java.util.ArrayList;

public class moba_MobaDataType extends MobaConstraintable, MobaApplicationFeature {

    private String name;
    private boolean time;
    private boolean array;
    private boolean numeric;
    private boolean decimal;
    private boolean primitive;
    private boolean date;
    private boolean timestamp;
    private boolean bool;
    private boolean string;
    private boolean predefined;
    private String dateFormatString;





    private moba_MobaDataType moba_mobadatatype;


    public moba_MobaDataType(
        String name,        boolean time,        boolean array,        boolean numeric,        boolean decimal,        boolean primitive,        boolean date,        boolean timestamp,        boolean bool,        boolean string,        boolean predefined,        String dateFormatString    ) {
        super(
        );
        this.name = name;
        this.time = time;
        this.array = array;
        this.numeric = numeric;
        this.decimal = decimal;
        this.primitive = primitive;
        this.date = date;
        this.timestamp = timestamp;
        this.bool = bool;
        this.string = string;
        this.predefined = predefined;
        this.dateFormatString = dateFormatString;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getTime() {
        return time;
    }

    public void setTime(boolean time) {
        this.time = time;
    }
    public boolean getArray() {
        return array;
    }

    public void setArray(boolean array) {
        this.array = array;
    }
    public boolean getNumeric() {
        return numeric;
    }

    public void setNumeric(boolean numeric) {
        this.numeric = numeric;
    }
    public boolean getDecimal() {
        return decimal;
    }

    public void setDecimal(boolean decimal) {
        this.decimal = decimal;
    }
    public boolean getPrimitive() {
        return primitive;
    }

    public void setPrimitive(boolean primitive) {
        this.primitive = primitive;
    }
    public boolean getDate() {
        return date;
    }

    public void setDate(boolean date) {
        this.date = date;
    }
    public boolean getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(boolean timestamp) {
        this.timestamp = timestamp;
    }
    public boolean getBool() {
        return bool;
    }

    public void setBool(boolean bool) {
        this.bool = bool;
    }
    public boolean getString() {
        return string;
    }

    public void setString(boolean string) {
        this.string = string;
    }
    public boolean getPredefined() {
        return predefined;
    }

    public void setPredefined(boolean predefined) {
        this.predefined = predefined;
    }
    public String getDateformatstring() {
        return dateFormatString;
    }

    public void setDateformatstring(String dateFormatString) {
        this.dateFormatString = dateFormatString;
    }

    public moba_MobaDataType getMoba_mobadatatype() {
        return moba_mobadatatype;
    }

    public void setMoba_mobadatatype(moba_MobaDataType moba_mobadatatype) {
        this.moba_mobadatatype = moba_mobadatatype;
    }

}