





import java.util.List;
import java.util.ArrayList;

public class myDsl_Directory extends AbstractFrontElement {

    private String name;
    private String purpose;





    private myDsl_Functionality mydsl_functionality;




    private myDsl_File mydsl_file;




    private myDsl_ReactApp mydsl_reactapp;




    private myDsl_Directory mydsl_directory;




    private myDsl_Action mydsl_action;


    public myDsl_Directory(
        String name,        String purpose    ) {
        super(
        );
        this.name = name;
        this.purpose = purpose;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPurpose() {
        return purpose;
    }

    public void setPurpose(String purpose) {
        this.purpose = purpose;
    }

    public myDsl_Functionality getMydsl_functionality() {
        return mydsl_functionality;
    }

    public void setMydsl_functionality(myDsl_Functionality mydsl_functionality) {
        this.mydsl_functionality = mydsl_functionality;
    }
    public myDsl_File getMydsl_file() {
        return mydsl_file;
    }

    public void setMydsl_file(myDsl_File mydsl_file) {
        this.mydsl_file = mydsl_file;
    }
    public myDsl_ReactApp getMydsl_reactapp() {
        return mydsl_reactapp;
    }

    public void setMydsl_reactapp(myDsl_ReactApp mydsl_reactapp) {
        this.mydsl_reactapp = mydsl_reactapp;
    }
    public myDsl_Directory getMydsl_directory() {
        return mydsl_directory;
    }

    public void setMydsl_directory(myDsl_Directory mydsl_directory) {
        this.mydsl_directory = mydsl_directory;
    }
    public myDsl_Action getMydsl_action() {
        return mydsl_action;
    }

    public void setMydsl_action(myDsl_Action mydsl_action) {
        this.mydsl_action = mydsl_action;
    }

}