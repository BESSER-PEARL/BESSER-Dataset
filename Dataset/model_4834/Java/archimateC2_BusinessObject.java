





import java.util.List;
import java.util.ArrayList;

public class archimateC2_BusinessObject extends PassiveStructure {






    private archimateC2_DataObject archimatec2_dataobject;




    private archimateC2_Representation archimatec2_representation;




    private List<archimateC2_DataObject> archimatec2_dataobjects;




    private List<archimateC2_BusinessEvent> archimatec2_businessevents;




    private archimateC2_Meaning archimatec2_meaning;




    private List<archimateC2_BusinessService> archimatec2_businessservices;




    private archimateC2_BusinessEvent archimatec2_businessevent;




    private List<archimateC2_Meaning> archimatec2_meanings;




    private archimateC2_BusinessService archimatec2_businessservice;




    private List<archimateC2_Representation> archimatec2_representations;


    public archimateC2_BusinessObject(
    ) {
        super(
        );
        this.archimatec2_dataobjects = new ArrayList<>();
        this.archimatec2_businessevents = new ArrayList<>();
        this.archimatec2_businessservices = new ArrayList<>();
        this.archimatec2_meanings = new ArrayList<>();
        this.archimatec2_representations = new ArrayList<>();
    }

    public archimateC2_BusinessObject(
        ArrayList<archimateC2_DataObject> archimatec2_dataobjects,        ArrayList<archimateC2_BusinessEvent> archimatec2_businessevents,        ArrayList<archimateC2_BusinessService> archimatec2_businessservices,        ArrayList<archimateC2_Meaning> archimatec2_meanings,        ArrayList<archimateC2_Representation> archimatec2_representations    ) {
        this.archimatec2_dataobjects = archimatec2_dataobjects;
        this.archimatec2_businessevents = archimatec2_businessevents;
        this.archimatec2_businessservices = archimatec2_businessservices;
        this.archimatec2_meanings = archimatec2_meanings;
        this.archimatec2_representations = archimatec2_representations;
    }


    public archimateC2_DataObject getArchimatec2_dataobject() {
        return archimatec2_dataobject;
    }

    public void setArchimatec2_dataobject(archimateC2_DataObject archimatec2_dataobject) {
        this.archimatec2_dataobject = archimatec2_dataobject;
    }
    public archimateC2_Representation getArchimatec2_representation() {
        return archimatec2_representation;
    }

    public void setArchimatec2_representation(archimateC2_Representation archimatec2_representation) {
        this.archimatec2_representation = archimatec2_representation;
    }
    public List<archimateC2_DataObject> getArchimatec2_dataobjects() {
        return archimatec2_dataobjects;
    }

    public void addArchimatec2_dataobject(Archimatec2_dataobject archimatec2_dataobject) {
        this.archimatec2_dataobjects.add(archimatec2_dataobject);
    }
    public List<archimateC2_BusinessEvent> getArchimatec2_businessevents() {
        return archimatec2_businessevents;
    }

    public void addArchimatec2_businessevent(Archimatec2_businessevent archimatec2_businessevent) {
        this.archimatec2_businessevents.add(archimatec2_businessevent);
    }
    public archimateC2_Meaning getArchimatec2_meaning() {
        return archimatec2_meaning;
    }

    public void setArchimatec2_meaning(archimateC2_Meaning archimatec2_meaning) {
        this.archimatec2_meaning = archimatec2_meaning;
    }
    public List<archimateC2_BusinessService> getArchimatec2_businessservices() {
        return archimatec2_businessservices;
    }

    public void addArchimatec2_businessservice(Archimatec2_businessservice archimatec2_businessservice) {
        this.archimatec2_businessservices.add(archimatec2_businessservice);
    }
    public archimateC2_BusinessEvent getArchimatec2_businessevent() {
        return archimatec2_businessevent;
    }

    public void setArchimatec2_businessevent(archimateC2_BusinessEvent archimatec2_businessevent) {
        this.archimatec2_businessevent = archimatec2_businessevent;
    }
    public List<archimateC2_Meaning> getArchimatec2_meanings() {
        return archimatec2_meanings;
    }

    public void addArchimatec2_meaning(Archimatec2_meaning archimatec2_meaning) {
        this.archimatec2_meanings.add(archimatec2_meaning);
    }
    public archimateC2_BusinessService getArchimatec2_businessservice() {
        return archimatec2_businessservice;
    }

    public void setArchimatec2_businessservice(archimateC2_BusinessService archimatec2_businessservice) {
        this.archimatec2_businessservice = archimatec2_businessservice;
    }
    public List<archimateC2_Representation> getArchimatec2_representations() {
        return archimatec2_representations;
    }

    public void addArchimatec2_representation(Archimatec2_representation archimatec2_representation) {
        this.archimatec2_representations.add(archimatec2_representation);
    }

}