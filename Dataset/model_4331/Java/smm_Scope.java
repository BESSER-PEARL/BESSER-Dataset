





import java.util.List;
import java.util.ArrayList;

public class smm_Scope extends SmmElement {

    private String recognizer;
    private String class_;
    private String name;
    private boolean enumerated;





    private List<smm_Measure> smm_measures;




    private smm_Measure smm_measure;


    public smm_Scope(
        String recognizer,        String class_,        String name,        boolean enumerated    ) {
        super(
        );
        this.recognizer = recognizer;
        this.class_ = class_;
        this.name = name;
        this.enumerated = enumerated;
        this.smm_measures = new ArrayList<>();
    }

    public smm_Scope(
        String recognizer,        String class_,        String name,        boolean enumerated        ArrayList<smm_Measure> smm_measures    ) {
        this.recognizer = recognizer;
        this.class_ = class_;
        this.name = name;
        this.enumerated = enumerated;
        this.smm_measures = smm_measures;
    }

    public String getRecognizer() {
        return recognizer;
    }

    public void setRecognizer(String recognizer) {
        this.recognizer = recognizer;
    }
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getEnumerated() {
        return enumerated;
    }

    public void setEnumerated(boolean enumerated) {
        this.enumerated = enumerated;
    }

    public List<smm_Measure> getSmm_measures() {
        return smm_measures;
    }

    public void addSmm_measure(Smm_measure smm_measure) {
        this.smm_measures.add(smm_measure);
    }
    public smm_Measure getSmm_measure() {
        return smm_measure;
    }

    public void setSmm_measure(smm_Measure smm_measure) {
        this.smm_measure = smm_measure;
    }

}