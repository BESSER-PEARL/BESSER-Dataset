





import java.util.List;
import java.util.ArrayList;

public class mutatorenvironment_ReplaceStringType extends StringType {

    private None newstring;
    private None oldstring;



    public mutatorenvironment_ReplaceStringType(
        None newstring,        None oldstring    ) {
        super(
        );
        this.newstring = newstring;
        this.oldstring = oldstring;
    }


    public None getNewstring() {
        return newstring;
    }

    public void setNewstring(None newstring) {
        this.newstring = newstring;
    }
    public None getOldstring() {
        return oldstring;
    }

    public void setOldstring(None oldstring) {
        this.oldstring = oldstring;
    }


}