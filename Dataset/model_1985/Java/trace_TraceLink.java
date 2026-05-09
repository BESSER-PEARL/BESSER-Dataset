





import java.util.List;
import java.util.ArrayList;

public class trace_TraceLink  {

    private String targetValue;
    private int requiredSimilarity;
    private String rationale;
    private String name;
    private int similarity;
    private String sourceValue;
    private int similarityMethod;





    private trace_Trace trace_trace;


    public trace_TraceLink(
        String targetValue,        int requiredSimilarity,        String rationale,        String name,        int similarity,        String sourceValue,        int similarityMethod    ) {
        this.targetValue = targetValue;
        this.requiredSimilarity = requiredSimilarity;
        this.rationale = rationale;
        this.name = name;
        this.similarity = similarity;
        this.sourceValue = sourceValue;
        this.similarityMethod = similarityMethod;
    }


    public String getTargetvalue() {
        return targetValue;
    }

    public void setTargetvalue(String targetValue) {
        this.targetValue = targetValue;
    }
    public int getRequiredsimilarity() {
        return requiredSimilarity;
    }

    public void setRequiredsimilarity(int requiredSimilarity) {
        this.requiredSimilarity = requiredSimilarity;
    }
    public String getRationale() {
        return rationale;
    }

    public void setRationale(String rationale) {
        this.rationale = rationale;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getSimilarity() {
        return similarity;
    }

    public void setSimilarity(int similarity) {
        this.similarity = similarity;
    }
    public String getSourcevalue() {
        return sourceValue;
    }

    public void setSourcevalue(String sourceValue) {
        this.sourceValue = sourceValue;
    }
    public int getSimilaritymethod() {
        return similarityMethod;
    }

    public void setSimilaritymethod(int similarityMethod) {
        this.similarityMethod = similarityMethod;
    }

    public trace_Trace getTrace_trace() {
        return trace_trace;
    }

    public void setTrace_trace(trace_Trace trace_trace) {
        this.trace_trace = trace_trace;
    }

}