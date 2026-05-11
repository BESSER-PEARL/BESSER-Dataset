





import java.util.List;
import java.util.ArrayList;

public class ecvi_Ecvi  {

    private String group1;
    private String cviNumber;
    private String issueDate;
    private String group;
    private String entryPermitNumber;
    private String expirationDate;
    private String speciesCode;
    private String shipmentDate;





    private ecvi_DocumentRoot ecvi_documentroot;




    private ecvi_Contact ecvi_contact;




    private List<ecvi_Animal> ecvi_animals;




    private List<ecvi_Attachement> ecvi_attachements;




    private ecvi_Accessions ecvi_accessions;




    private ecvi_Contact ecvi_contact;


    public ecvi_Ecvi(
        String group1,        String cviNumber,        String issueDate,        String group,        String entryPermitNumber,        String expirationDate,        String speciesCode,        String shipmentDate    ) {
        this.group1 = group1;
        this.cviNumber = cviNumber;
        this.issueDate = issueDate;
        this.group = group;
        this.entryPermitNumber = entryPermitNumber;
        this.expirationDate = expirationDate;
        this.speciesCode = speciesCode;
        this.shipmentDate = shipmentDate;
        this.ecvi_animals = new ArrayList<>();
        this.ecvi_attachements = new ArrayList<>();
    }

    public ecvi_Ecvi(
        String group1,        String cviNumber,        String issueDate,        String group,        String entryPermitNumber,        String expirationDate,        String speciesCode,        String shipmentDate        ArrayList<ecvi_Animal> ecvi_animals,        ArrayList<ecvi_Attachement> ecvi_attachements    ) {
        this.group1 = group1;
        this.cviNumber = cviNumber;
        this.issueDate = issueDate;
        this.group = group;
        this.entryPermitNumber = entryPermitNumber;
        this.expirationDate = expirationDate;
        this.speciesCode = speciesCode;
        this.shipmentDate = shipmentDate;
        this.ecvi_animals = ecvi_animals;
        this.ecvi_attachements = ecvi_attachements;
    }

    public String getGroup1() {
        return group1;
    }

    public void setGroup1(String group1) {
        this.group1 = group1;
    }
    public String getCvinumber() {
        return cviNumber;
    }

    public void setCvinumber(String cviNumber) {
        this.cviNumber = cviNumber;
    }
    public String getIssuedate() {
        return issueDate;
    }

    public void setIssuedate(String issueDate) {
        this.issueDate = issueDate;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getEntrypermitnumber() {
        return entryPermitNumber;
    }

    public void setEntrypermitnumber(String entryPermitNumber) {
        this.entryPermitNumber = entryPermitNumber;
    }
    public String getExpirationdate() {
        return expirationDate;
    }

    public void setExpirationdate(String expirationDate) {
        this.expirationDate = expirationDate;
    }
    public String getSpeciescode() {
        return speciesCode;
    }

    public void setSpeciescode(String speciesCode) {
        this.speciesCode = speciesCode;
    }
    public String getShipmentdate() {
        return shipmentDate;
    }

    public void setShipmentdate(String shipmentDate) {
        this.shipmentDate = shipmentDate;
    }

    public ecvi_DocumentRoot getEcvi_documentroot() {
        return ecvi_documentroot;
    }

    public void setEcvi_documentroot(ecvi_DocumentRoot ecvi_documentroot) {
        this.ecvi_documentroot = ecvi_documentroot;
    }
    public ecvi_Contact getEcvi_contact() {
        return ecvi_contact;
    }

    public void setEcvi_contact(ecvi_Contact ecvi_contact) {
        this.ecvi_contact = ecvi_contact;
    }
    public List<ecvi_Animal> getEcvi_animals() {
        return ecvi_animals;
    }

    public void addEcvi_animal(Ecvi_animal ecvi_animal) {
        this.ecvi_animals.add(ecvi_animal);
    }
    public List<ecvi_Attachement> getEcvi_attachements() {
        return ecvi_attachements;
    }

    public void addEcvi_attachement(Ecvi_attachement ecvi_attachement) {
        this.ecvi_attachements.add(ecvi_attachement);
    }
    public ecvi_Accessions getEcvi_accessions() {
        return ecvi_accessions;
    }

    public void setEcvi_accessions(ecvi_Accessions ecvi_accessions) {
        this.ecvi_accessions = ecvi_accessions;
    }
    public ecvi_Contact getEcvi_contact() {
        return ecvi_contact;
    }

    public void setEcvi_contact(ecvi_Contact ecvi_contact) {
        this.ecvi_contact = ecvi_contact;
    }

}