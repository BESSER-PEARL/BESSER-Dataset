





import java.util.List;
import java.util.ArrayList;

public class myDsl_DirectoryContent  {

    private String name;





    private myDsl_SegmentStructureContent mydsl_segmentstructurecontent;




    private List<myDsl_EObject> mydsl_eobjects;


    public myDsl_DirectoryContent(
        String name    ) {
        this.name = name;
        this.mydsl_eobjects = new ArrayList<>();
    }

    public myDsl_DirectoryContent(
        String name        ArrayList<myDsl_EObject> mydsl_eobjects    ) {
        this.name = name;
        this.mydsl_eobjects = mydsl_eobjects;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_SegmentStructureContent getMydsl_segmentstructurecontent() {
        return mydsl_segmentstructurecontent;
    }

    public void setMydsl_segmentstructurecontent(myDsl_SegmentStructureContent mydsl_segmentstructurecontent) {
        this.mydsl_segmentstructurecontent = mydsl_segmentstructurecontent;
    }
    public List<myDsl_EObject> getMydsl_eobjects() {
        return mydsl_eobjects;
    }

    public void addMydsl_eobject(Mydsl_eobject mydsl_eobject) {
        this.mydsl_eobjects.add(mydsl_eobject);
    }

}