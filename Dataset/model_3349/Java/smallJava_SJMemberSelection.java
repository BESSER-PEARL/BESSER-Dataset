





import java.util.List;
import java.util.ArrayList;

public class smallJava_SJMemberSelection extends SJExpression {

    private boolean methodinvocation;





    private smallJava_SJExpression smalljava_sjexpression;




    private smallJava_SJMember smalljava_sjmember;




    private List<smallJava_SJExpression> smalljava_sjexpressions;


    public smallJava_SJMemberSelection(
        boolean methodinvocation    ) {
        super(
        );
        this.methodinvocation = methodinvocation;
        this.smalljava_sjexpressions = new ArrayList<>();
    }

    public smallJava_SJMemberSelection(
        boolean methodinvocation        ArrayList<smallJava_SJExpression> smalljava_sjexpressions    ) {
        this.methodinvocation = methodinvocation;
        this.smalljava_sjexpressions = smalljava_sjexpressions;
    }

    public boolean getMethodinvocation() {
        return methodinvocation;
    }

    public void setMethodinvocation(boolean methodinvocation) {
        this.methodinvocation = methodinvocation;
    }

    public smallJava_SJExpression getSmalljava_sjexpression() {
        return smalljava_sjexpression;
    }

    public void setSmalljava_sjexpression(smallJava_SJExpression smalljava_sjexpression) {
        this.smalljava_sjexpression = smalljava_sjexpression;
    }
    public smallJava_SJMember getSmalljava_sjmember() {
        return smalljava_sjmember;
    }

    public void setSmalljava_sjmember(smallJava_SJMember smalljava_sjmember) {
        this.smalljava_sjmember = smalljava_sjmember;
    }
    public List<smallJava_SJExpression> getSmalljava_sjexpressions() {
        return smalljava_sjexpressions;
    }

    public void addSmalljava_sjexpression(Smalljava_sjexpression smalljava_sjexpression) {
        this.smalljava_sjexpressions.add(smalljava_sjexpression);
    }

}