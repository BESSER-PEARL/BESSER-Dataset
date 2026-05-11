





import java.util.List;
import java.util.ArrayList;

public class smallJava_SJExpression extends SJStatement {






    private smallJava_SJReturn smalljava_sjreturn;




    private smallJava_SJIfStatement smalljava_sjifstatement;




    private smallJava_SJVariableDeclaration smalljava_sjvariabledeclaration;


    public smallJava_SJExpression(
    ) {
        super(
        );
    }



    public smallJava_SJReturn getSmalljava_sjreturn() {
        return smalljava_sjreturn;
    }

    public void setSmalljava_sjreturn(smallJava_SJReturn smalljava_sjreturn) {
        this.smalljava_sjreturn = smalljava_sjreturn;
    }
    public smallJava_SJIfStatement getSmalljava_sjifstatement() {
        return smalljava_sjifstatement;
    }

    public void setSmalljava_sjifstatement(smallJava_SJIfStatement smalljava_sjifstatement) {
        this.smalljava_sjifstatement = smalljava_sjifstatement;
    }
    public smallJava_SJVariableDeclaration getSmalljava_sjvariabledeclaration() {
        return smalljava_sjvariabledeclaration;
    }

    public void setSmalljava_sjvariabledeclaration(smallJava_SJVariableDeclaration smalljava_sjvariabledeclaration) {
        this.smalljava_sjvariabledeclaration = smalljava_sjvariabledeclaration;
    }

}