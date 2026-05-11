





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedStereotype extends TracedClass {






    private uml_TracedProfile uml_tracedprofile;




    private List<uml_TracedImage> uml_tracedimages;


    public umlTrace_uml_TracedStereotype(
    ) {
        super(
        );
        this.uml_tracedimages = new ArrayList<>();
    }

    public umlTrace_uml_TracedStereotype(
        ArrayList<uml_TracedImage> uml_tracedimages    ) {
        this.uml_tracedimages = uml_tracedimages;
    }


    public uml_TracedProfile getUml_tracedprofile() {
        return uml_tracedprofile;
    }

    public void setUml_tracedprofile(uml_TracedProfile uml_tracedprofile) {
        this.uml_tracedprofile = uml_tracedprofile;
    }
    public List<uml_TracedImage> getUml_tracedimages() {
        return uml_tracedimages;
    }

    public void addUml_tracedimage(Uml_tracedimage uml_tracedimage) {
        this.uml_tracedimages.add(uml_tracedimage);
    }

}