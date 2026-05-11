





import java.util.List;
import java.util.ArrayList;

public class ecvi_Laboratory  {

    private String accessionNumber;
    private String labName;
    private String accessionDate;
    private String premId;





    private ecvi_Accession ecvi_accession;


    public ecvi_Laboratory(
        String accessionNumber,        String labName,        String accessionDate,        String premId    ) {
        this.accessionNumber = accessionNumber;
        this.labName = labName;
        this.accessionDate = accessionDate;
        this.premId = premId;
    }


    public String getAccessionnumber() {
        return accessionNumber;
    }

    public void setAccessionnumber(String accessionNumber) {
        this.accessionNumber = accessionNumber;
    }
    public String getLabname() {
        return labName;
    }

    public void setLabname(String labName) {
        this.labName = labName;
    }
    public String getAccessiondate() {
        return accessionDate;
    }

    public void setAccessiondate(String accessionDate) {
        this.accessionDate = accessionDate;
    }
    public String getPremid() {
        return premId;
    }

    public void setPremid(String premId) {
        this.premId = premId;
    }

    public ecvi_Accession getEcvi_accession() {
        return ecvi_accession;
    }

    public void setEcvi_accession(ecvi_Accession ecvi_accession) {
        this.ecvi_accession = ecvi_accession;
    }

}