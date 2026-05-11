





import java.util.List;
import java.util.ArrayList;

public class smallJava_SJMemberSelection extends SJExpression {

    private boolean methodinvocation;





    private smallJava_SJMember smalljava_sjmember;


    public smallJava_SJMemberSelection(
        boolean methodinvocation    ) {
        super(
        );
        this.methodinvocation = methodinvocation;
    }


    public boolean getMethodinvocation() {
        return methodinvocation;
    }

    public void setMethodinvocation(boolean methodinvocation) {
        this.methodinvocation = methodinvocation;
    }

    public smallJava_SJMember getSmalljava_sjmember() {
        return smalljava_sjmember;
    }

    public void setSmalljava_sjmember(smallJava_SJMember smalljava_sjmember) {
        this.smalljava_sjmember = smalljava_sjmember;
    }

}