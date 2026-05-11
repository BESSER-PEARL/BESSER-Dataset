





import java.util.List;
import java.util.ArrayList;

public class adb_LabelisableStatement  {






    private List<adb_Label> adb_labels;




    private adb_SequenceOfStatements adb_sequenceofstatements;


    public adb_LabelisableStatement(
    ) {
        this.adb_labels = new ArrayList<>();
    }

    public adb_LabelisableStatement(
        ArrayList<adb_Label> adb_labels    ) {
        this.adb_labels = adb_labels;
    }


    public List<adb_Label> getAdb_labels() {
        return adb_labels;
    }

    public void addAdb_label(Adb_label adb_label) {
        this.adb_labels.add(adb_label);
    }
    public adb_SequenceOfStatements getAdb_sequenceofstatements() {
        return adb_sequenceofstatements;
    }

    public void setAdb_sequenceofstatements(adb_SequenceOfStatements adb_sequenceofstatements) {
        this.adb_sequenceofstatements = adb_sequenceofstatements;
    }

}