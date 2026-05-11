





import java.util.List;
import java.util.ArrayList;

public class TokenTrace_Token extends MultiLiteralConstraint {

    private int referenceCount;
    private String assignedProbability;
    private String scale;
    private String name;
    private String message;
    private String computedProbability;
    private String tokenType;





    private TokenTrace_Token tokentrace_token;




    private TokenTrace_TokenTrace tokentrace_tokentrace;




    private TokenTrace_TokenTrace tokentrace_tokentrace;


    public TokenTrace_Token(
        int referenceCount,        String assignedProbability,        String scale,        String name,        String message,        String computedProbability,        String tokenType    ) {
        super(
        );
        this.referenceCount = referenceCount;
        this.assignedProbability = assignedProbability;
        this.scale = scale;
        this.name = name;
        this.message = message;
        this.computedProbability = computedProbability;
        this.tokenType = tokenType;
    }


    public int getReferencecount() {
        return referenceCount;
    }

    public void setReferencecount(int referenceCount) {
        this.referenceCount = referenceCount;
    }
    public String getAssignedprobability() {
        return assignedProbability;
    }

    public void setAssignedprobability(String assignedProbability) {
        this.assignedProbability = assignedProbability;
    }
    public String getScale() {
        return scale;
    }

    public void setScale(String scale) {
        this.scale = scale;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getComputedprobability() {
        return computedProbability;
    }

    public void setComputedprobability(String computedProbability) {
        this.computedProbability = computedProbability;
    }
    public String getTokentype() {
        return tokenType;
    }

    public void setTokentype(String tokenType) {
        this.tokenType = tokenType;
    }

    public TokenTrace_Token getTokentrace_token() {
        return tokentrace_token;
    }

    public void setTokentrace_token(TokenTrace_Token tokentrace_token) {
        this.tokentrace_token = tokentrace_token;
    }
    public TokenTrace_TokenTrace getTokentrace_tokentrace() {
        return tokentrace_tokentrace;
    }

    public void setTokentrace_tokentrace(TokenTrace_TokenTrace tokentrace_tokentrace) {
        this.tokentrace_tokentrace = tokentrace_tokentrace;
    }
    public TokenTrace_TokenTrace getTokentrace_tokentrace() {
        return tokentrace_tokentrace;
    }

    public void setTokentrace_tokentrace(TokenTrace_TokenTrace tokentrace_tokentrace) {
        this.tokentrace_tokentrace = tokentrace_tokentrace;
    }

}