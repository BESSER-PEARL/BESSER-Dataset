





import java.util.List;
import java.util.ArrayList;

public class jdtmm_JDTMethod extends JDTMember {

    private String abstract;
    private String synchronized;
    private String final;
    private String constructor;
    private String static;



    public jdtmm_JDTMethod(
        String abstract,        String synchronized,        String final,        String constructor,        String static    ) {
        super(
        );
        this.abstract = abstract;
        this.synchronized = synchronized;
        this.final = final;
        this.constructor = constructor;
        this.static = static;
    }


    public String getAbstract() {
        return abstract;
    }

    public void setAbstract(String abstract) {
        this.abstract = abstract;
    }
    public String getSynchronized() {
        return synchronized;
    }

    public void setSynchronized(String synchronized) {
        this.synchronized = synchronized;
    }
    public String getFinal() {
        return final;
    }

    public void setFinal(String final) {
        this.final = final;
    }
    public String getConstructor() {
        return constructor;
    }

    public void setConstructor(String constructor) {
        this.constructor = constructor;
    }
    public String getStatic() {
        return static;
    }

    public void setStatic(String static) {
        this.static = static;
    }


}