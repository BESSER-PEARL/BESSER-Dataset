





import java.util.List;
import java.util.ArrayList;

public class presentation_DateTimeDeclType  {

    private String mixed;
    private String source;
    private String dataStyleName;
    private String name;



    public presentation_DateTimeDeclType(
        String mixed,        String source,        String dataStyleName,        String name    ) {
        this.mixed = mixed;
        this.source = source;
        this.dataStyleName = dataStyleName;
        this.name = name;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getDatastylename() {
        return dataStyleName;
    }

    public void setDatastylename(String dataStyleName) {
        this.dataStyleName = dataStyleName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}