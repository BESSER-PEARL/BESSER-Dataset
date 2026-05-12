





import java.util.List;
import java.util.ArrayList;

public class qsar_MetadataType  {

    private String responseLabel;
    private String datasetname;
    private String uRL;
    private String license;
    private String authors;
    private String responsePlacement;
    private String description;





    private qsar_QsarType qsar_qsartype;


    public qsar_MetadataType(
        String responseLabel,        String datasetname,        String uRL,        String license,        String authors,        String responsePlacement,        String description    ) {
        this.responseLabel = responseLabel;
        this.datasetname = datasetname;
        this.uRL = uRL;
        this.license = license;
        this.authors = authors;
        this.responsePlacement = responsePlacement;
        this.description = description;
    }


    public String getResponselabel() {
        return responseLabel;
    }

    public void setResponselabel(String responseLabel) {
        this.responseLabel = responseLabel;
    }
    public String getDatasetname() {
        return datasetname;
    }

    public void setDatasetname(String datasetname) {
        this.datasetname = datasetname;
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
    public String getAuthors() {
        return authors;
    }

    public void setAuthors(String authors) {
        this.authors = authors;
    }
    public String getResponseplacement() {
        return responsePlacement;
    }

    public void setResponseplacement(String responsePlacement) {
        this.responsePlacement = responsePlacement;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public qsar_QsarType getQsar_qsartype() {
        return qsar_qsartype;
    }

    public void setQsar_qsartype(qsar_QsarType qsar_qsartype) {
        this.qsar_qsartype = qsar_qsartype;
    }

}