





import java.util.List;
import java.util.ArrayList;

public class ctrlflow101_Function extends SequenceNode {






    private List<ctrlflow101_Sequence> ctrlflow101_sequences;




    private List<ctrlflow101_Token> ctrlflow101_tokens;




    private ctrlflow101_Function ctrlflow101_function;


    public ctrlflow101_Function(
    ) {
        super(
        );
        this.ctrlflow101_sequences = new ArrayList<>();
        this.ctrlflow101_tokens = new ArrayList<>();
    }

    public ctrlflow101_Function(
        ArrayList<ctrlflow101_Sequence> ctrlflow101_sequences,        ArrayList<ctrlflow101_Token> ctrlflow101_tokens    ) {
        this.ctrlflow101_sequences = ctrlflow101_sequences;
        this.ctrlflow101_tokens = ctrlflow101_tokens;
    }


    public List<ctrlflow101_Sequence> getCtrlflow101_sequences() {
        return ctrlflow101_sequences;
    }

    public void addCtrlflow101_sequence(Ctrlflow101_sequence ctrlflow101_sequence) {
        this.ctrlflow101_sequences.add(ctrlflow101_sequence);
    }
    public List<ctrlflow101_Token> getCtrlflow101_tokens() {
        return ctrlflow101_tokens;
    }

    public void addCtrlflow101_token(Ctrlflow101_token ctrlflow101_token) {
        this.ctrlflow101_tokens.add(ctrlflow101_token);
    }
    public ctrlflow101_Function getCtrlflow101_function() {
        return ctrlflow101_function;
    }

    public void setCtrlflow101_function(ctrlflow101_Function ctrlflow101_function) {
        this.ctrlflow101_function = ctrlflow101_function;
    }

}