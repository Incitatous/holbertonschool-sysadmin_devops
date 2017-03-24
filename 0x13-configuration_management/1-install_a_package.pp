# Installs puppet-lint 2.1.1
package { 'puppet-lint':
  ensure   => 'latest',
  provider => 'gem',
}
