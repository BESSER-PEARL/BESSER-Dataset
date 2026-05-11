





import java.util.List;
import java.util.ArrayList;

public class archimateC2_ApplicationService extends ArchimateElement {






    private archimateC2_ApplicationFunction archimatec2_applicationfunction;




    private archimateC2_ApplicationFunction archimatec2_applicationfunction;




    private archimateC2_ApplicationInterface archimatec2_applicationinterface;




    private archimateC2_DataObject archimatec2_dataobject;




    private List<archimateC2_ApplicationFunction> archimatec2_applicationfunctions;




    private List<archimateC2_ApplicationInterface> archimatec2_applicationinterfaces;




    private List<archimateC2_ApplicationFunction> archimatec2_applicationfunctions;




    private List<archimateC2_DataObject> archimatec2_dataobjects;


    public archimateC2_ApplicationService(
    ) {
        super(
        );
        this.archimatec2_applicationfunctions = new ArrayList<>();
        this.archimatec2_applicationinterfaces = new ArrayList<>();
        this.archimatec2_applicationfunctions = new ArrayList<>();
        this.archimatec2_dataobjects = new ArrayList<>();
    }

    public archimateC2_ApplicationService(
        ArrayList<archimateC2_ApplicationFunction> archimatec2_applicationfunctions,        ArrayList<archimateC2_ApplicationInterface> archimatec2_applicationinterfaces,        ArrayList<archimateC2_ApplicationFunction> archimatec2_applicationfunctions,        ArrayList<archimateC2_DataObject> archimatec2_dataobjects    ) {
        this.archimatec2_applicationfunctions = archimatec2_applicationfunctions;
        this.archimatec2_applicationinterfaces = archimatec2_applicationinterfaces;
        this.archimatec2_applicationfunctions = archimatec2_applicationfunctions;
        this.archimatec2_dataobjects = archimatec2_dataobjects;
    }


    public archimateC2_ApplicationFunction getArchimatec2_applicationfunction() {
        return archimatec2_applicationfunction;
    }

    public void setArchimatec2_applicationfunction(archimateC2_ApplicationFunction archimatec2_applicationfunction) {
        this.archimatec2_applicationfunction = archimatec2_applicationfunction;
    }
    public archimateC2_ApplicationFunction getArchimatec2_applicationfunction() {
        return archimatec2_applicationfunction;
    }

    public void setArchimatec2_applicationfunction(archimateC2_ApplicationFunction archimatec2_applicationfunction) {
        this.archimatec2_applicationfunction = archimatec2_applicationfunction;
    }
    public archimateC2_ApplicationInterface getArchimatec2_applicationinterface() {
        return archimatec2_applicationinterface;
    }

    public void setArchimatec2_applicationinterface(archimateC2_ApplicationInterface archimatec2_applicationinterface) {
        this.archimatec2_applicationinterface = archimatec2_applicationinterface;
    }
    public archimateC2_DataObject getArchimatec2_dataobject() {
        return archimatec2_dataobject;
    }

    public void setArchimatec2_dataobject(archimateC2_DataObject archimatec2_dataobject) {
        this.archimatec2_dataobject = archimatec2_dataobject;
    }
    public List<archimateC2_ApplicationFunction> getArchimatec2_applicationfunctions() {
        return archimatec2_applicationfunctions;
    }

    public void addArchimatec2_applicationfunction(Archimatec2_applicationfunction archimatec2_applicationfunction) {
        this.archimatec2_applicationfunctions.add(archimatec2_applicationfunction);
    }
    public List<archimateC2_ApplicationInterface> getArchimatec2_applicationinterfaces() {
        return archimatec2_applicationinterfaces;
    }

    public void addArchimatec2_applicationinterface(Archimatec2_applicationinterface archimatec2_applicationinterface) {
        this.archimatec2_applicationinterfaces.add(archimatec2_applicationinterface);
    }
    public List<archimateC2_ApplicationFunction> getArchimatec2_applicationfunctions() {
        return archimatec2_applicationfunctions;
    }

    public void addArchimatec2_applicationfunction(Archimatec2_applicationfunction archimatec2_applicationfunction) {
        this.archimatec2_applicationfunctions.add(archimatec2_applicationfunction);
    }
    public List<archimateC2_DataObject> getArchimatec2_dataobjects() {
        return archimatec2_dataobjects;
    }

    public void addArchimatec2_dataobject(Archimatec2_dataobject archimatec2_dataobject) {
        this.archimatec2_dataobjects.add(archimatec2_dataobject);
    }

}