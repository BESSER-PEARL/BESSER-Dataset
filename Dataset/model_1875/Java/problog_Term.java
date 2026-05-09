





import java.util.List;
import java.util.ArrayList;

public class problog_Term  {

    private int arguments;
    private String name;





    private problog_ProbLogProgram problog_problogprogram;


    public problog_Term(
        int arguments,        String name    ) {
        this.arguments = arguments;
        this.name = name;
    }


    public int getArguments() {
        return arguments;
    }

    public void setArguments(int arguments) {
        this.arguments = arguments;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public problog_ProbLogProgram getProblog_problogprogram() {
        return problog_problogprogram;
    }

    public void setProblog_problogprogram(problog_ProbLogProgram problog_problogprogram) {
        this.problog_problogprogram = problog_problogprogram;
    }

}