





import java.util.List;
import java.util.ArrayList;

public class sample_Sentence  {

    private String Text;





    private sample_Then sample_then;




    private sample_When sample_when;




    private sample_Annotation sample_annotation;




    private sample_Given sample_given;




    private List<sample_Variable> sample_variables;


    public sample_Sentence(
        String Text    ) {
        this.Text = Text;
        this.sample_variables = new ArrayList<>();
    }

    public sample_Sentence(
        String Text        ArrayList<sample_Variable> sample_variables    ) {
        this.Text = Text;
        this.sample_variables = sample_variables;
    }

    public String getText() {
        return Text;
    }

    public void setText(String Text) {
        this.Text = Text;
    }

    public sample_Then getSample_then() {
        return sample_then;
    }

    public void setSample_then(sample_Then sample_then) {
        this.sample_then = sample_then;
    }
    public sample_When getSample_when() {
        return sample_when;
    }

    public void setSample_when(sample_When sample_when) {
        this.sample_when = sample_when;
    }
    public sample_Annotation getSample_annotation() {
        return sample_annotation;
    }

    public void setSample_annotation(sample_Annotation sample_annotation) {
        this.sample_annotation = sample_annotation;
    }
    public sample_Given getSample_given() {
        return sample_given;
    }

    public void setSample_given(sample_Given sample_given) {
        this.sample_given = sample_given;
    }
    public List<sample_Variable> getSample_variables() {
        return sample_variables;
    }

    public void addSample_variable(Sample_variable sample_variable) {
        this.sample_variables.add(sample_variable);
    }

}