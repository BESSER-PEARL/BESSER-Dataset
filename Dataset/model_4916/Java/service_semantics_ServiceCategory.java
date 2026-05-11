





import java.util.List;
import java.util.ArrayList;

public class service_semantics_ServiceCategory  {

    private String taxonomy;
    private String code;
    private String name;
    private String value;



    public service_semantics_ServiceCategory(
        String taxonomy,        String code,        String name,        String value    ) {
        this.taxonomy = taxonomy;
        this.code = code;
        this.name = name;
        this.value = value;
    }


    public String getTaxonomy() {
        return taxonomy;
    }

    public void setTaxonomy(String taxonomy) {
        this.taxonomy = taxonomy;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}