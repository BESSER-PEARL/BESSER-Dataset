





import java.util.List;
import java.util.ArrayList;

public class qsar_MetadataType  {

    private String datasetname;
    private String description;
    private String authors;
    private String uRL;
    private String license;





    private qsar_QsarType qsar_qsartype;


    public qsar_MetadataType(
        String datasetname,        String description,        String authors,        String uRL,        String license    ) {
        this.datasetname = datasetname;
        this.description = description;
        this.authors = authors;
        this.uRL = uRL;
        this.license = license;
    }


    public String getDatasetname() {
        return datasetname;
    }

    public void setDatasetname(String datasetname) {
        this.datasetname = datasetname;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getAuthors() {
        return authors;
    }

    public void setAuthors(String authors) {
        this.authors = authors;
    }
    public String getUrl() {
        return uRL;
    }

    public void setUrl(String uRL) {
        this.uRL = uRL;
    }
    public String getLicense() {
        return license;
    }

    public void setLicense(String license) {
        this.license = license;
    }

    public qsar_QsarType getQsar_qsartype() {
        return qsar_qsartype;
    }

    public void setQsar_qsartype(qsar_QsarType qsar_qsartype) {
        this.qsar_qsartype = qsar_qsartype;
    }

}