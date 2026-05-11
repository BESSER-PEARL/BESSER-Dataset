





import java.util.List;
import java.util.ArrayList;

public class myDsl_LiteralType  {






    private myDsl_MapType mydsl_maptype;




    private myDsl_StructType mydsl_structtype;




    private myDsl_TypeName mydsl_typename;




    private myDsl_CompositeLit mydsl_compositelit;


    public myDsl_LiteralType(
    ) {
    }



    public myDsl_MapType getMydsl_maptype() {
        return mydsl_maptype;
    }

    public void setMydsl_maptype(myDsl_MapType mydsl_maptype) {
        this.mydsl_maptype = mydsl_maptype;
    }
    public myDsl_StructType getMydsl_structtype() {
        return mydsl_structtype;
    }

    public void setMydsl_structtype(myDsl_StructType mydsl_structtype) {
        this.mydsl_structtype = mydsl_structtype;
    }
    public myDsl_TypeName getMydsl_typename() {
        return mydsl_typename;
    }

    public void setMydsl_typename(myDsl_TypeName mydsl_typename) {
        this.mydsl_typename = mydsl_typename;
    }
    public myDsl_CompositeLit getMydsl_compositelit() {
        return mydsl_compositelit;
    }

    public void setMydsl_compositelit(myDsl_CompositeLit mydsl_compositelit) {
        this.mydsl_compositelit = mydsl_compositelit;
    }

}