





import java.util.List;
import java.util.ArrayList;

public class libraryElement_InterfaceList  {






    private List<libraryElement_AdapterDeclaration> libraryelement_adapterdeclarations;




    private libraryElement_FBNetworkElement libraryelement_fbnetworkelement;




    private List<libraryElement_VarDeclaration> libraryelement_vardeclarations;




    private List<libraryElement_VarDeclaration> libraryelement_vardeclarations;




    private List<libraryElement_Event> libraryelement_events;




    private libraryElement_FBType libraryelement_fbtype;




    private List<libraryElement_AdapterDeclaration> libraryelement_adapterdeclarations;




    private List<libraryElement_Event> libraryelement_events;


    public libraryElement_InterfaceList(
    ) {
        this.libraryelement_adapterdeclarations = new ArrayList<>();
        this.libraryelement_vardeclarations = new ArrayList<>();
        this.libraryelement_vardeclarations = new ArrayList<>();
        this.libraryelement_events = new ArrayList<>();
        this.libraryelement_adapterdeclarations = new ArrayList<>();
        this.libraryelement_events = new ArrayList<>();
    }

    public libraryElement_InterfaceList(
        ArrayList<libraryElement_AdapterDeclaration> libraryelement_adapterdeclarations,        ArrayList<libraryElement_VarDeclaration> libraryelement_vardeclarations,        ArrayList<libraryElement_VarDeclaration> libraryelement_vardeclarations,        ArrayList<libraryElement_Event> libraryelement_events,        ArrayList<libraryElement_AdapterDeclaration> libraryelement_adapterdeclarations,        ArrayList<libraryElement_Event> libraryelement_events    ) {
        this.libraryelement_adapterdeclarations = libraryelement_adapterdeclarations;
        this.libraryelement_vardeclarations = libraryelement_vardeclarations;
        this.libraryelement_vardeclarations = libraryelement_vardeclarations;
        this.libraryelement_events = libraryelement_events;
        this.libraryelement_adapterdeclarations = libraryelement_adapterdeclarations;
        this.libraryelement_events = libraryelement_events;
    }


    public List<libraryElement_AdapterDeclaration> getLibraryelement_adapterdeclarations() {
        return libraryelement_adapterdeclarations;
    }

    public void addLibraryelement_adapterdeclaration(Libraryelement_adapterdeclaration libraryelement_adapterdeclaration) {
        this.libraryelement_adapterdeclarations.add(libraryelement_adapterdeclaration);
    }
    public libraryElement_FBNetworkElement getLibraryelement_fbnetworkelement() {
        return libraryelement_fbnetworkelement;
    }

    public void setLibraryelement_fbnetworkelement(libraryElement_FBNetworkElement libraryelement_fbnetworkelement) {
        this.libraryelement_fbnetworkelement = libraryelement_fbnetworkelement;
    }
    public List<libraryElement_VarDeclaration> getLibraryelement_vardeclarations() {
        return libraryelement_vardeclarations;
    }

    public void addLibraryelement_vardeclaration(Libraryelement_vardeclaration libraryelement_vardeclaration) {
        this.libraryelement_vardeclarations.add(libraryelement_vardeclaration);
    }
    public List<libraryElement_VarDeclaration> getLibraryelement_vardeclarations() {
        return libraryelement_vardeclarations;
    }

    public void addLibraryelement_vardeclaration(Libraryelement_vardeclaration libraryelement_vardeclaration) {
        this.libraryelement_vardeclarations.add(libraryelement_vardeclaration);
    }
    public List<libraryElement_Event> getLibraryelement_events() {
        return libraryelement_events;
    }

    public void addLibraryelement_event(Libraryelement_event libraryelement_event) {
        this.libraryelement_events.add(libraryelement_event);
    }
    public libraryElement_FBType getLibraryelement_fbtype() {
        return libraryelement_fbtype;
    }

    public void setLibraryelement_fbtype(libraryElement_FBType libraryelement_fbtype) {
        this.libraryelement_fbtype = libraryelement_fbtype;
    }
    public List<libraryElement_AdapterDeclaration> getLibraryelement_adapterdeclarations() {
        return libraryelement_adapterdeclarations;
    }

    public void addLibraryelement_adapterdeclaration(Libraryelement_adapterdeclaration libraryelement_adapterdeclaration) {
        this.libraryelement_adapterdeclarations.add(libraryelement_adapterdeclaration);
    }
    public List<libraryElement_Event> getLibraryelement_events() {
        return libraryelement_events;
    }

    public void addLibraryelement_event(Libraryelement_event libraryelement_event) {
        this.libraryelement_events.add(libraryelement_event);
    }

}