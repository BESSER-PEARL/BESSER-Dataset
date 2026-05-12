





import java.util.List;
import java.util.ArrayList;

public class qsar_ResponseunitType  {

    private String description;
    private String name;
    private String id;
    private String uRL;
    private String shortname;





    private qsar_QsarType qsar_qsartype;


    public qsar_ResponseunitType(
        String description,        String name,        String id,        String uRL,        String shortname    ) {
        this.description = description;
        this.name = name;
        this.id = id;
        this.uRL = uRL;
        this.shortname = shortname;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getUrl() {
        return uRL;
    }

    public void setUrl(String uRL) {
        this.uRL = uRL;
    }
    public String getShortname() {
        return shortname;
    }

    public void setShortname(String shortname) {
        this.shortname = shortname;
    }

    public qsar_QsarType getQsar_qsartype() {
        return qsar_qsartype;
    }

    public void setQsar_qsartype(qsar_QsarType qsar_qsartype) {
        this.qsar_qsartype = qsar_qsartype;
    }

}