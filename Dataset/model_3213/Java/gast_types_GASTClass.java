





import java.util.List;
import java.util.ArrayList;

public class gast_types_GASTClass extends types_Member, types_GASTType {

    private boolean anonymous;
    private boolean interface;
    private int linesOfComments;
    private boolean primitive;
    private boolean local;
    private boolean inner;





    private List<Delegate> delegates;




    private List<GASTClass> gastclasss;




    private GASTClass gastclass;




    private List<GASTClass> gastclasss;




    private List<Function> functions;




    private List<Access> accesss;




    private List<TypeAlias> typealiass;




    private Function function;




    private List<GASTClass> gastclasss;




    private List<GASTClass> gastclasss;




    private GASTClass gastclass;




    private Package package;


    public gast_types_GASTClass(
        boolean anonymous,        boolean interface,        int linesOfComments,        boolean primitive,        boolean local,        boolean inner    ) {
        super(
        );
        this.anonymous = anonymous;
        this.interface = interface;
        this.linesOfComments = linesOfComments;
        this.primitive = primitive;
        this.local = local;
        this.inner = inner;
        this.delegates = new ArrayList<>();
        this.gastclasss = new ArrayList<>();
        this.gastclasss = new ArrayList<>();
        this.functions = new ArrayList<>();
        this.accesss = new ArrayList<>();
        this.typealiass = new ArrayList<>();
        this.gastclasss = new ArrayList<>();
        this.gastclasss = new ArrayList<>();
    }

    public gast_types_GASTClass(
        boolean anonymous,        boolean interface,        int linesOfComments,        boolean primitive,        boolean local,        boolean inner        ArrayList<Delegate> delegates,        ArrayList<GASTClass> gastclasss,        ArrayList<GASTClass> gastclasss,        ArrayList<Function> functions,        ArrayList<Access> accesss,        ArrayList<TypeAlias> typealiass,        ArrayList<GASTClass> gastclasss,        ArrayList<GASTClass> gastclasss    ) {
        this.anonymous = anonymous;
        this.interface = interface;
        this.linesOfComments = linesOfComments;
        this.primitive = primitive;
        this.local = local;
        this.inner = inner;
        this.delegates = delegates;
        this.gastclasss = gastclasss;
        this.gastclasss = gastclasss;
        this.functions = functions;
        this.accesss = accesss;
        this.typealiass = typealiass;
        this.gastclasss = gastclasss;
        this.gastclasss = gastclasss;
    }

    public boolean getAnonymous() {
        return anonymous;
    }

    public void setAnonymous(boolean anonymous) {
        this.anonymous = anonymous;
    }
    public boolean getInterface() {
        return interface;
    }

    public void setInterface(boolean interface) {
        this.interface = interface;
    }
    public int getLinesofcomments() {
        return linesOfComments;
    }

    public void setLinesofcomments(int linesOfComments) {
        this.linesOfComments = linesOfComments;
    }
    public boolean getPrimitive() {
        return primitive;
    }

    public void setPrimitive(boolean primitive) {
        this.primitive = primitive;
    }
    public boolean getLocal() {
        return local;
    }

    public void setLocal(boolean local) {
        this.local = local;
    }
    public boolean getInner() {
        return inner;
    }

    public void setInner(boolean inner) {
        this.inner = inner;
    }

    public List<Delegate> getDelegates() {
        return delegates;
    }

    public void addDelegate(Delegate delegate) {
        this.delegates.add(delegate);
    }
    public List<GASTClass> getGastclasss() {
        return gastclasss;
    }

    public void addGastclass(Gastclass gastclass) {
        this.gastclasss.add(gastclass);
    }
    public GASTClass getGastclass() {
        return gastclass;
    }

    public void setGastclass(GASTClass gastclass) {
        this.gastclass = gastclass;
    }
    public List<GASTClass> getGastclasss() {
        return gastclasss;
    }

    public void addGastclass(Gastclass gastclass) {
        this.gastclasss.add(gastclass);
    }
    public List<Function> getFunctions() {
        return functions;
    }

    public void addFunction(Function function) {
        this.functions.add(function);
    }
    public List<Access> getAccesss() {
        return accesss;
    }

    public void addAccess(Access access) {
        this.accesss.add(access);
    }
    public List<TypeAlias> getTypealiass() {
        return typealiass;
    }

    public void addTypealias(Typealias typealias) {
        this.typealiass.add(typealias);
    }
    public Function getFunction() {
        return function;
    }

    public void setFunction(Function function) {
        this.function = function;
    }
    public List<GASTClass> getGastclasss() {
        return gastclasss;
    }

    public void addGastclass(Gastclass gastclass) {
        this.gastclasss.add(gastclass);
    }
    public List<GASTClass> getGastclasss() {
        return gastclasss;
    }

    public void addGastclass(Gastclass gastclass) {
        this.gastclasss.add(gastclass);
    }
    public GASTClass getGastclass() {
        return gastclass;
    }

    public void setGastclass(GASTClass gastclass) {
        this.gastclass = gastclass;
    }
    public Package getPackage() {
        return package;
    }

    public void setPackage(Package package) {
        this.package = package;
    }

}