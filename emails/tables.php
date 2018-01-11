<!DOCTYPE html>
<html lang="en">
<?php
    //Create Connection with MySQL Database
    $con = mysqli_connect('127.0.0.1','root','houses123');

    //Select Database
    if(!mysqli_select_db($con,'emailing'))
    {
        echo "Database Not Selected";
    }
    ?>

<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">
  <title>SB Admin - Start Bootstrap Template</title>
  <!-- Bootstrap core CSS-->
  <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
  <!-- Custom fonts for this template-->
  <link href="vendor/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
  <!-- Page level plugin CSS-->
  <link href="vendor/datatables/dataTables.bootstrap4.css" rel="stylesheet">
  <!-- Custom styles for this template-->
  <link href="css/sb-admin.css" rel="stylesheet">
</head>

<body class="fixed-nav sticky-footer bg-dark" id="page-top">
  <!-- Navigation-->
  <nav class="navbar navbar-expand-lg navbar-dark fixed-top" id="mainNav" style="background-color: #000000" >
    <a class="navbar-brand" href="#"><span><b><img src="wso2.png" width="70" height="35"></b>&nbsp&nbsp Email Analysis</span>
      <a class="navbar-brand" href="index.html"></a>
    
    <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarResponsive">
      <ul class="navbar-nav navbar-sidenav" id="exampleAccordion">
        <li class="nav-item" data-toggle="tooltip" data-placement="right" title="Email Analysis">
          <a class="nav-link" href="index.html">
            <i class="fa fa-envelope"></i>
            <span class="nav-link-text" >Email Analysis</span>
          </a>
        </li>
        <li class="nav-item" data-toggle="tooltip" data-placement="right" title="Complexity Level">
          <a class="nav-link" href="charts.html">
            <i class="fa fa-book"></i>
            <span class="nav-link-text">Complexity Analysis</span>
          </a>
        </li>
        <li class="nav-item" data-toggle="tooltip" data-placement="right" title="Sentiment Analysis">
          <a class="nav-link" href="tables.php">
            <i class="fa fa-frown-o"></i>
            <span class="nav-link-text">Sentiment Analysis</span>
          </a>
        
        </li>


        
      </ul>
      <ul class="navbar-nav sidenav-toggler">
        <li class="nav-item">
          <a class="nav-link text-center" id="sidenavToggler">
            <i class="fa fa-fw fa-angle-left"></i>
          </a>
        </li>
      </ul>
      <ul class="navbar-nav ml-auto">
        
        <li class="nav-item">
          <a class="nav-link" data-toggle="modal" data-target="#exampleModal">
            <i class="fa fa-fw fa-sign-out"></i>Logout</a>
        </li>
      </ul>
    </div>
  </nav>


  <div class="content-wrapper">
    <div class="container-fluid">
      <!-- Breadcrumbs-->
      <ol class="breadcrumb">
        <li class="breadcrumb-item">
          <a style="color:#000000" href="index.html">Email Analysis</a>

        </li>
        <li class="breadcrumb-item active">Sentiment Analysis</li>
      </ol>
      <!-- Example DataTables Card-->
      <div class="card mb-3">
        <div class="card-header">
          <i class="fa fa-frown-o"></i> Sentiment Levels




          
          </div>

        <div class="card-body">

        

          <div class="table-responsive">
            <table class="table table-bordered" id="dataTable" width="100%" cellspacing="0">
              <thead>
                <tr>
                  <th> Date </th>
                  <th> Subject </th>
                  <th> Very Postive </th>
                  <th> Postive </th>
                  <th> Neutral </th>
                  <th> Negative </th>
                  <th> Very Negative </th>
                  <th> Overall </th>
                  <th> Sender(Last Message) </th>
                  <th> Groups </th>
                </tr>
                  <tbody>
    <?php
    /*//Create Connection with MySQL Database
    $con = mysqli_connect('127.0.0.1','root','houses123');

    //Select Database
    if(!mysqli_select_db($con,'emailing'))
    {
        echo "Database Not Selected";
    }*/
    //Select Query
    #$sql = "SELECT * FROM sentiment";

    $query = "SELECT DISTINCT overall FROM sentiment";

    //Execute the SQL query
    
    $grpnames = mysqli_query($con,$query);

          $raw_results="SELECT * FROM sentiment";
            
            
            $run=mysqli_query($con,$raw_results);

            while($row = mysqli_fetch_array($run)){

              echo "<tr>";
              echo "<td>".$row['date']."</td>";


              /*echo "<td>" . 
              '<a href="cards.php?data='.urlencode($row['sub']).'&data2='.urlencode($row['lastmsg']).'">'.$row['sub'] . '</a>' ."</td>";*/

              echo "<td>" .'<a target="_blank" href='.$row['lastmsg'].'>'.$row['sub'] .'</a>'."</td>";


              echo "<td>".$row['vpositive']."</td>";
              echo "<td>".$row['positive']."</td>";
              echo "<td>".$row['neutral']."</td>";

              if ($row['emotionalLevel'] == "-1"){
              echo "<td>".'<div class="bg-danger text-white">'.$row['negative'].'</div>'."</td>";
              }
              else {
                echo "<td>".$row['negative']."</td>";
              }

              if ($row['emotionalLevel'] == "-2"){
              echo "<td>".'<div class="bg-danger text-white">'.$row['vnegative'].'</div>'."</td>";
              }
              else {
                echo "<td>".$row['vnegative']."</td>";
              }
              
              echo "<td>".$row['overall']."</td>";
              echo "<td>".$row['sender']."</td>";
              echo "<td>".$row['groupname']."</td>";
        
          }
        
    

    ?>
  </tbody>
            </table>
          </div>
        
    </div>

    <!-- /.container-fluid-->
    <!-- /.content-wrapper-->
    <!-- <footer class="sticky-footer">
      <div class="container">
        <div class="text-center">
          <small>Copyright © Your Website 2017</small>
        </div>
      </div>
    </footer> -->
    <!-- Scroll to Top Button-->
    <a class="scroll-to-top rounded" href="#page-top">
      <i class="fa fa-angle-up"></i>
    </a>
    <!-- Logout Modal-->
    <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Ready to Leave?</h5>
            <button class="close" type="button" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">×</span>
            </button>
          </div>
          <div class="modal-body">Select "Logout" below if you are ready to end your current session.</div>
          <div class="modal-footer">
            <button class="btn btn-secondary" type="button" data-dismiss="modal">Cancel</button>
            <a class="btn btn-primary" href="login.html">Logout</a>
          </div>
        </div>
      </div>
    </div>
    <!-- Bootstrap core JavaScript-->
    <script src="vendor/jquery/jquery.min.js"></script>
    <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
    <!-- Core plugin JavaScript-->
    <script src="vendor/jquery-easing/jquery.easing.min.js"></script>
    <!-- Page level plugin JavaScript-->
    <script src="vendor/datatables/jquery.dataTables.js"></script>
    <script src="vendor/datatables/dataTables.bootstrap4.js"></script>
    <!-- Custom scripts for all pages-->
    <script src="js/sb-admin.min.js"></script>
    <!-- Custom scripts for this page-->
    <script src="js/sb-admin-datatables.min.js"></script>
  </div>

</body>

</html>
